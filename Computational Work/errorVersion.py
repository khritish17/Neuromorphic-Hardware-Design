import pandas as pd
import random as rnd 
data=pd.read_csv('characterDataSet1.csv')
dataWrite=open('newCharacterDataSet.csv','w')

dataWrite.write("x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,y,character\n")
# print(data)
final_string=""
error_count=3
no_of_dataSets=20
for a in range(no_of_dataSets):
    for j in range(26):
        a=[]
        count=0
        while(count<=error_count):
            r=rnd.randint(1,35)
            if r not in a:
                a.append(r)
                count+=1

        for i in range(1,36):
            columnLabels="x{}".format(i)
            value=str(data[columnLabels][j])
            
            if i in a:
                if value=='0':
                    value='1'
                else:
                    value='0'
            final_string=final_string+"{},".format(value)
        value=str(data['y'][j])
        final_string+="{},".format(value)

        value=str(data['character'][j])
        final_string+="{}\n".format(value)
        dataWrite.write(final_string)
        


        final_string=""