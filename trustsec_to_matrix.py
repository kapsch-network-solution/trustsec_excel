import csv

tags={}
i=0
data = ""

with open('matrix.csv', newline='') as csvfile:
    raw = csv.reader(csvfile, delimiter=',', quotechar='|')

    #get all the sgts
    for row in raw:
        #read first field for tag name, ignore first line
        if i != 0:
            tags[row[0]] = ""
            keys = list(tags.keys())
        i=i+1

matrix = [[0 for _ in range(len(tags))] for _ in range(len(tags))]

i=0
with open('matrix.csv', newline='') as csvfile:
    raw = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in raw:
        #read first field for tag name, ignore first line
        if i != 0:
            #print("Index of "+row[0]+ " " + str(keys.index(row[0])))
            matrix[keys.index(row[0])][keys.index(row[1])] = row[2]
        i=i+1

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
        data = data + matrix[i][z] + ","
    data = data + "\n"

#write database
f = open("demofile2.csv", "w")
f.write(data)
f.close()
