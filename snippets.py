
#print string n times
n = 2
s ="Programming"

print(s * n)

#chunks a list into smaller lists
def chunk(list, size):
    return [list[i:i+size] for i in range(0,len(list), size)]
y=chunk([1,2,3,4,5,6],2)
print(y)


#Using join
hobbies = ["basketball", "football", "swimming"]

print("My hobbies are:") # My hobbies are:
print(", ".join(hobbies))

#using split
def split(word):
    return [i for i in word]
word="consultadd"
print(split(word))

#merging two dictionaries

def merge_two_dicts(a, b):
    c = a.copy()   # make a copy of a 
    c.update(b)    # modify keys and values of a with the ones from b
    return c


a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}

#another way
print(merge_two_dicts(a, b)) 
def merge_dictionaries(a, b):
   return {**a, **b}


a = { 'x': 1, 'y': 2}
b = { 'y': 3, 'z': 4}
print(merge_dictionaries(a, b))


#using zip
def to_dictionary(keys, values):
    return dict(zip(keys, values))

keys = ["a", "b", "c"]    
values = [2, 3, 4]
print(to_dictionary(keys, values))

#using enumerate
list = ["a", "b", "c", "d"]
for index, element in enumerate(list): 
    print("Value", element, "Index ", index, )


#getting vowels
def get_vowels(string):
    return [each for each in string if each  in 'aeiou'] 


print(get_vowels('foobar'))# ['o', 'o', 'a']
get_vowels('gym') # []

#using palindrom
def palindrome(a):
    return a == a[::-1]

print(palindrome('mom'))






































