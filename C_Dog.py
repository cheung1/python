

class Animal(object):

    # initialize
    def __init__(self, name):
        self.name = name


    # before the killed
    def __del__(self):
        print(".....aaa....aaa......")


dog = Animal("wangcai")


print("---------------1----------")

dog1 = dog
dog2 = dog

print(dog)
print(dog1)
print(dog2)

print("--------------2-----------")


del dog
del dog1
del dog2

print("--------------3-----------")

# though didnt invoke the '__del__()' method,then who did it?
# python will invoke the method by itself,then kill it

