# trustsec_excel
[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/kapsch-network-solution/trustsec_excel)

This script converts the ISE trustsec matrix export to a more ISE web gui like version which can be loaded in EXCEL and edited. Once the offline edit is complete you can convert it back to normal ISE syntax so you can import it again

Export Trustsec matrix in ISE (make sure you activate the "Include empty cells export)

![Trustsec matrix export](https://i.ibb.co/F8ZTWnf/ise-export.png)

**ISE Export/Import version**

![before](https://i.ibb.co/LZ1ftMs/before.png)

**Excel version**

![after](https://i.ibb.co/NKd1B52/after.png)


![excel](https://i.ibb.co/LS5vRTD/excel.png)
## Requirements
none. Script uses just python native libraries

## Installation

``` 
git clone https://github.com/catachan/trustsec_excel.git
cd trustsec_excel
```

Create virtual enviroment (optional)

``` 
python3 -m trustsec_excel
source trustsec_excel/bin/activate
```


## Export

from ISE to EXCEL
``` 
python trustsec_excel.py -e <ISE_CSV_FILENAME> <EXCEL_CSV_FILENAME>
``` 

**Example usage**
``` 
python trustsec_excel.py -e sample.csv excel_sample.csv
``` 
This command takes the CSV file sample.csv which was exported from an ISE installation and converts it into EXCEL format file excel_sample.csv. You can then edit the different cells ( = SGACL action) for your needs.

## Import
from EXCEL to ISE
``` 
python trustsec_excel.py -i <EXCEL_CSV_FILENAME> <ISE_CSV_FILENAME> 
``` 

**Example usage**
``` 
python trustsec_excel.py -i excel_sample.csv sample.csv 
``` 
This command takes the CSV file excel_sample.csv which was converted before with the -e option and convert it back into the file sample.csv which can be imported back into ISE.

## Limitations
* Order of SGTs in vertical/horizontal axis in excel csv must be the same
* All cells will be enabled (disabled, monitoring is not working in this script)

## Convert to windows exe
To convert the python file use python package auto-py-to-exe.exe
pip install auto-py-to-exe
auto-py-to-exe
