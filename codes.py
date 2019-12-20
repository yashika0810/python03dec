#print string n times
n=2
s='Consultadd'
print(s*n)


#Chunks a list into smaller lists

def random(list,size):
    return [list[i:i+size] for i in range(0,len(list), size)]

y=random([1,2,3,4,5,6],2)
print(y)

#using join

training=['Java','Python','AWS']
print("The trainings are:")
print(" ".join(training))

#using split

def split(word):
    return [i for i in word]
word="consultadd"
print(split(word))


# merge two dictionaries

def merge(a,b):
    return {**a,**b}
    return c
a={'a':1,'b':3,'c':3}
b={1:5,4:5,7:33}
print(merge(a,b))

def get_vowels(string):
    return [i for i in string if i not in 'aieou']
print(get_vowels("Consultadd"))


