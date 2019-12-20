'''try:
    filehandler=open('data.txt','r')
    content=filehandler.read()
    print(content)

except:
    print("Please provide the correct name of file")
finally:
    filehandler.close()

from sys import argv
name_of_program, filename=argv

print("Name of program is", name_of_program)
print("Name of file is", filename)


while True:
    try:
        fh=open(filename)
        content=fh.read()
        print(content)
        fh.close()
        break
    except:
        print("The name entered is wrong. Please provide correct name")
        try_again=input("DO you want to try again!! Press yes (Y) or no (N)")
        
        if try_again=='Y':
             filename= input("Please enter the name correctly this time")
        else:
            break
    

import csv
with open('testing.csv') as csvfile:
   result = csv.reader(csvfile)
   for i in result:
       print(i)


x=[1,2,3,4,5]
for i in range(len(x)):
    x[i]=x[i]*2
print(x)
'''

my_list=[]
for i in [20,40,60]:
    for j in [2,4,6]:
        my_list.append(i*j)
print(my_list)
