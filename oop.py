'''class candidate:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def customfunc(self): #not received automatically
        print("Coming from customfunc and my name is", self.name)

obj=candidate("Yashika",24)
print(obj.customfunc()) #automatically passed



#Inheritance


class consultadd:     #parent/base/super
    def __init__(self,domain):
        self.domain=domain
    def getname(self):
        return self.domain
    def candidateattending(self):
        return False

class pcandidate(consultadd):   #child
    def candidateattending(self):
        return True

c=consultadd("Python")
print(c.getname(),c.candidateattending())
p=pcandidate("Java")
print(p.getname(),p.candidateattending())

'''
#Polymorphism-->  


class candidate:
    def domain(self):
        print("I am learning Python")
    def language(self):
        print("I am student of python")
    def level(self):
        print("Intermediate")

class trainer:
    def domain(self):
        print("I train on Python")
    def language(self):
        print("I am a trainer")
    def level(self):
        print("Expert")


c=candidate()
t=trainer()
for i in (c,t):
    i.domain()
    i.language()
    i.level()

