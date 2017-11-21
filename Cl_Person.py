


class Person(object):
    def __init__(self, name, age):
        self.__name = name   # private attribution
        self.__age = age
        self.high = 180   # share attribution

    def __str__(self):
        return 'the age is : ' + str(self.__age)

    def setNewAge(self,newAge):
        if 80 > newAge > 0:
            self.__age = newAge

    def getAge(self):
        return self.__age

xiaoming = Person('xiaoming',18)
print(xiaoming)
#xiaoming.__age = 119
#print(xiaoming.__age)

xiaoming.setNewAge(119)
print(xiaoming)


ageTemp = xiaoming.getAge()
print(ageTemp)
