
#class className:

 #   methods

#define a class
#Class Dog
class Dog:
    
    #defina a method
    
    def __init__(self,newName,newWeight,newColor):
        self.weight = newWeight
        self.color = newColor
        self.name = newName

    def bark(self):
        print 'Wang...Wang..Wang...'

    def run(self):
        print 'dog is running '

    def eat(self):
        print 'dog can eat foods '
    # in methods ,can change the properties
        self.weight += 5

    def printName(self):
        print 'My name is %s'%self.name

#create a dog
doggie = Dog('BigBat'5,'white')


#get doggies properties
printName()
print doggie.weight
print doggie.color

wangcai = Dog(10,'yello')

print wangcai.weight
print wangcai.color
