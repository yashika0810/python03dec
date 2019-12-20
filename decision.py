'''x=10
y=20
if x>y:
    print("x is greater")
else:
    print("y is greater")


x=int(input("Enter a number"))

if x<0:
    if x>-5:
        print("result is greater than -5")
    else:
        print("result is less than -5")
  
elif x==0:
    print("Result is 0")
elif x>0 and x<30:
    print("result is positive and less than 30")
else:
    print("Result is greater than 30")

while True:
    print("Enter any number but -1 will quit the loop and -2 will keep you in the loop")
    x=int(input("Give any choice"))
    if x==-1:
        break
    if x==-2:
        continue
        print("I am inside the loop")
print("I am outside the loop")



avg=0
total=0
count=0
print("Enter the grade (-1 to quit)")
grade=int(input("Enter the grade"))
while grade!=-1:
    total=total+grade
    count=count+1
    print("Enter the grade (-1 to quit)")
    grade=int(input("Enter the grade"))
    if count==4:
        break

print("I am outside the loop")
avg=total/count
print("Avg of subjects is",avg)
'''



