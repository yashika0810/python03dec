x=[1,2,3,4,5,6]
'''for i in x:
    print("List elements:",i)
    
print("The list has", len(x), "elements")

# range(len(x))--> len(x)-->range(6)-->0,1,2,3,4,5
for i in range(len(x)):
    x[i]=x[i]*5
print(x)


#1+2+3+4+5
sum=0
for val in range(1,6):
    sum=sum+val
print(sum)



for i in range(3):
    for x in range(10,14):
        for y in range(100,104):
            print(i,x,y)


x=[1,5,9,7]
for elements in x:
    if elements%2==0:
        print("The list contains an even no")
        break
#This else executes only if break is NEVER reached and loop is terminated after all iterations
else:
    print("The list does not contain even no")


for i in range(1,10):
    if(i%5==0):
        break
    print(i)

print("Hey I am here")


#n=5
#{1:1,2:4,3:9,4:16,5:25}

n=int(input("Enter any no"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)
'''

#s="consultadd123"
#LETTER:3 DIGITS:8

#s=csAhcCnhwCU 
#isupper(), islower()

s=input("Enter any sentence")
d={"DIGITS":0, "LETTER":0}
for i in s:
    if i.isdigit():
        d["DIGITS"]+=1
    elif i.isalpha():
        d["LETTER"]+=1
    else:
        pass #executes nothing

print("LETTERS:", d["LETTER"])
print("DIGITS:", d["DIGITS"])



