

class Animal(object):

    # initialize
    def __init__(self, name = 'animal', color = 'white'):
        self.name = name
        self.color = color

    # before the killed
    def __del__(self):
        print(".....aaa....aaa......")





class Dog(Animal):
    # initialize
    #def __init__(self, name = 'dog', color = 'white'):
    #    self.__name = name
    #    self.__color = color

    # before the killed
    #def __del__(self):
    #    print(".....aaa....aaa......")

    def printInfo(self):
        print("the name is %s"%self.name)
        print("the color is %s"%self.color)

wangcai = Dog(name = 'wangcai')
wangcai.printInfo()
