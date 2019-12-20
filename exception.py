'''while True:
    try:
        x=int(input("enter value of x"))
        y=int(input("enter value of y"))
        avg=(x+y)/2
        print(avg)
    except Exception as e:
        print(e)
        print("Please provide an integer value")
    finally:
        print("Always print")'''

with open("data.txt", "r") as file:
    data=file.readline()
    for i in data:
        word=i.split()
        print(word)
        


