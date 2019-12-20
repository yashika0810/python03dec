'''# with argument with return type
def add(p,q):    # function definition # Formal parameters
    result=p+q
    return result
z=add(10,30)    #function calling   # Actual parameters
print(z) 

# without argument with return type
def add():
    print("This is the second type")
    a=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    return a*b
x=add()
print(x)
'''
# with argument without return type

def add(a,b):
    print("this is the third type")
    print(a+b)
x=add(19,40)
print(x)
print(type(x))

# without argument without return type

# without argument with return type
def add():
    print("This is the fourth type")
    a=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    print(a+b)
x=add()
print(x)
print(type(x))
