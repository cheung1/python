
#class className:

 #   methods

#define a class
#Class Dog
class Dog:
    
    #defina a method
    #dog is barking
    def bark(self):
        print 'Wang...Wang..Wang...'

    def run(self):
        print 'dog is running '

    def eat(self):
        print 'dog can eat foods '
    # in methods ,can change the properties
        self.weight += 5

#create a dog
doggie = Dog()
#invoke a methon of Dog
doggie.bark()
doggie.run()

#add properties
doggie.weight = 5
doggie.color = 'white'

#get doggies properties
print doggie.weight
print doggie.color

#invoke eat,will change the weight 
doggie.eat()
print doggie.weight
