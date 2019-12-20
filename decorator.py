def decorator(func):
    def inner():  #wrapper function
        print("This is before execution")
        x=int(input("enter value of x"))
        y=int(input("enter value of y"))
        res=x+y
        print(res)
        func()
    return inner

#Main code starts here

@decorator
def need():
    print("Hello I need to be decorated")
#need=decorator(need)
need()
