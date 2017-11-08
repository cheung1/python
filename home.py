
#define a class named Home
class Home:
    def __init__(self,area):
        self.area = area
        self.accomodateItem = []
    
    def __str__(self):
        msg =  'Your home area u can use is : ' + str(self.area)
        return msg

    def containItem(self,item):

        #if self.area > item.size:
        #    self.accomodateItem.append(item)
        #    self.area -= item.size
        #    print 'add %s is correct,the valible area is : %d'%(item.name,self.area)
        #else:
        #    print 'error: the %s area is bigger than ur home'%item.name


        # this way can secret the information
        bedArea = item.getBedArea()
        if self.area > bedArea:
            self.accomodateItem.append(item)
            self.area -= bedArea
            print 'add %s is correct,the valible area is : %d'%(item.getBedName(),self.area)
        else:
            print 'error: the %s area is bigger than ur home'%item.getBedName()




#define another class named Bed
class Bed:

    def __init__(self,name,size):
        self.size = size
        self.name = name

    def __str__(self):
        msg = 'The bed ' + self.name + ' size is : ' + str(self.size)
        return msg

    def getBedArea(self):
        return self.size

    def getBedName(self):
        return self.name

home = Home(150)
print home



bed = Bed('Ximengsi',4)
print bed

home.containItem(bed)
print home

bed.getBedArea()

bed2 = Bed('wood',10)
home.containItem(bed2)
print home

bed3 = Bed('Bigsize',180)
home.containItem(bed3)
print home
