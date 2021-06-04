from csv import writer
from datetime import date
from datetime import datetime
#from seq_number import * 
import csv
import sys

path='/home/test/home/scripts/'
filename= sys.argv[1] #name of the file

path_file = path + filename

today = date.today()
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

with open("seq_number.xml","r") as seq:
    data = seq.read()
    data2= data.split("=")
    seq_str=data2[1]
    seq = int(seq_str)
    seq_original = seq
    print(seq)

#f = open("financial_data_20210501", "a+")

f = open('processing.out','a')

with open(path_file, newline='') as fin:
    r = csv.DictReader(fin)
    lines = list(r)


    with open(path_file,'w',newline='') as f_object:
        w = csv.DictWriter(f_object, fieldnames= r.fieldnames + 'seq_number'.split())

        for line in lines:
            emlist = {'seq_number': seq}
            line.update(emlist)
            w.writerow(line)
            seq = seq + 1
            
            #f = open('precessing.out','a')
            f.write(date_time +   "      SEQ_INSERTION      INFO    " + str(seq) + "\n")
            print(seq)

f_object.close()

f.close()

fan =  open("seq_number.xml","rt")
data = fan.read()
data = data.replace(str(seq_original), str(seq))
fan.close()

finw = open("seq_number.xml","wt")
finw.write(data)
finw.close()

