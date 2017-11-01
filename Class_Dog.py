
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
