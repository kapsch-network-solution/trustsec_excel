import csv
import sys
import difflib
import re

# function to convert ISE export to excel format
def func_export(original_file,new_file):
    tags={}
    i=0
    data = ""

    #open file and get list of SGTs first
    with open(original_file, newline='') as csvfile:
        raw = csv.reader(csvfile, delimiter=',', quotechar='|')

        #get all the sgts
        for row in raw:
            #read first field for tag name, ignore first line
            if i != 0:
                tags[row[0]] = ""
                keys = list(tags.keys())
            i=i+1

    # create a 2d matrix with length of number of SGTs
    matrix = [[0 for _ in range(len(tags))] for _ in range(len(tags))]

    #populate matrix
    i=0
    with open(original_file, newline='') as csvfile:
        raw = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in raw:
            #read first field for tag name, ignore first line
            if i != 0:
                #print("Index of "+row[0]+ " " + str(keys.index(row[0])))
                celldata = row[2] + "|" + row[3]
                matrix[keys.index(row[0])][keys.index(row[1])] = celldata
            i=i+1

    # code for writing into new file
    #build first csv line
    i=0
    for i in range(len(keys)):
        data = data + ","+keys[i]
    data = data +"\n"

    # build other lines 
    i=0
    for i in range(len(keys)):
        data = data + keys[i]+","
        z=0
        for z in range(len(keys)):
            if z == len(keys)-1:
                data = data + matrix[i][z]
            else:
                data = data + matrix[i][z] + ","
        data = data + "\n"

    #write file 
    f = open(new_file, "w")
    f.write(data)
    f.close()

# function to convert EXCEL table so it can be imported back into ise
def func_import(original_file,new_file):
    i = 0
    j = 0
    sgts = []

    data = "Source SGT:String(32):Required,Destination SGT:String(32):Required,SGACL Name:String(32):Required,Rule Status:String(enabled|disabled|monitor):Required\n"

    with open(original_file, newline='') as csvfile:

        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        raw = csv.reader(csvfile, dialect)
        #raw = csv.reader(raw_data, delimiter=',', quotechar='|')

        for row in raw:
            #first line code
            if i == 0:
                for tags in range(len(row)):
                    if tags != 0:
                        sgts.append(row[tags])
            else:
                #DEBUG
                #print(row)
                for j in range(len(row)):
                    if j != 0:
                        celldata = row[j].split('|')
                        #data = data + row[0] + "," + sgts[j-1]+  "," + row[j] +",enabled\n"
                        data = data + row[0] + "," + sgts[j-1]+  "," + celldata[0] +","+celldata[1]+"\n"
            i = i+1

    #write file
    f = open(new_file, "w")
    f.write(data)
    f.close()       

def func_compare(original_file,new_file):

    print("Newfile: " + new_file)
    print("Oldfile: " + original_file)
    
    with open(original_file) as original:
        original_data = original.readlines()
        original_data.sort()

    with open(new_file) as new:
        new_data = new.readlines()
        new_data.sort()

    list_difference = []
    for item in new_data:
        if item not in original_data:
          list_difference.append(item)

    if len(list_difference) == 0:
        print("##### No changes found ####")
    else:
        print("##### Changes found ####")
        for change in list_difference:
            print("New: " + change)

            details = change.split(',')
            regex = details[0]+","+details[1]+",.*"

            pat = re.compile(regex)
            old = [i for i in original_data if pat.match(i)]
            print("Old: " +old[0])
 
            print("==========================================") 

# main section
if len(sys.argv) == 4:
    original_file = sys.argv[2]
    new_file = sys.argv[3]

    if sys.argv[1] == "-e":
        func_export(original_file,new_file)
    elif sys.argv[1] == "-i":
        func_import(original_file,new_file)
    elif sys.argv[1] == "-c":
        func_compare(original_file,new_file)
    else:
        print("Usage " + sys.argv[0] + "-i/-e/-c <sourcefile> <destinationfile>")
else:
    print("Usage " + sys.argv[0] + "-i/-e/-c <sourcefile> <destinationfile>")
