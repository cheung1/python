#student management system

#1. design a frame,,,,dont think function first
# through the analysis ,the fellow code need to be put in a function
def showInfo():
	print '-'*30
	print '            Student Management system V1.0             '
	print '1.add student information'
	print '2.delete student information'
	print '3.mend student information'
	print '4.search student information'
	print '5.list the  stu#student management system

#1. design a frame,,,,dont think function first
# through the analysis ,the fellow code need to be put in a function
def showInfo():
	print '-'*30
	print '            Student Management system V1.0             '
	print '1.add student information'
	print '2.delete student information'
	print '3.mend student information'
	print '4.search student information'
	print '5.list the  student information'
	print '6.quit the system'
	print '-'*30

def addNewStu(studentsTemp):
    #can add the information
    #stuInfo = {'name':'','id':'','age':''}
    #[{},{}]

    name = raw_input('please input name : ')
    stuId = input('please input stuId : ')
    age = input('please input age : ')

    #have a dict,then it has value and key,then can append	
    stuInfo = {}
    stuInfo['name'] = name
    stuInfo['id'] = stuId
    stuInfo['age'] = age
    studentsTemp.append(stuInfo)


def nestingStu(studentsTemp):
    print '-'*20
    print 'next,will show all the students information'
    print ' id          name            age'
    for temp in studentsTemp:
        print ' %s           %s             %s'%(temp['id'],temp['name'],temp['age'])
    print '-'*20

def delStuInfo(students):
    print '-'*20
    delNum = input('please input the order:')

    #students = [{'name':'xiaowang','id':111,'age':18}]
    #del students[0]

    del students[delNum]
    print '-'*20

def mendStuInfo(students):
    print '-'*20
    mendNum = input('please input the order : ')
    #students = [{'name':'xiaowang','id':111,'age':18}]
    #for x in students:
    #    x['name'] = 'xiaoli'
    #    x['id'] = 222
    #    x['age'] = 12
    #wamt to show the information first , then mend it 
    #for i,n,a in students[menNum]:
    #print ' %s           %s             %s'%(temp['id'],temp['name'],temp['age'])
    mendName = raw_input('please input the new name : ')
    mendId = raw_input('please input the new id : ')
    mendAge = raw_input('please input the new age : ')
        
    #have a dict,then it has value and key,then can mend it
    mendInfo = students[mendNum]
    mendInfo['name'] = mendName
    mendInfo['id'] = mendId
    mendInfo['age'] = mendAge
    print '-'*20

def searchStuInfo(Tempstudents):
     #can use the dic ,accordint to the key to situated value..what should i do in the first step.
     #first,let the user choose which key he want to find
    searchInfo = raw_input('please input what is the key you want to use??>>------ [name/id/age] : ')
    if searchInfo == 'name':
        searchName = raw_input('please input the name : ')
        print '-'*20
        for temp in Tempstudents:
            #for searchName in temp.get('name'):
            if temp.get('name') == searchName:
                print ' Name is %s ,id is %s,age is %s'%(temp['name'],temp['id'],temp['age'])
                break
            else:
                print 'cannot find this name'
                break
        print '-'*20
    elif searchInfo == 'id':
        searchId = input('please input the id : ')
        print '-'*20
        for temp in Tempstudents:
            #for searchName in temp.get('name'):
            if temp.get('id') == searchId:
                print ' Name is %s ,id is %s,age is %s'%(temp['name'],temp['id'],temp['age'])
                break
            else:
                print 'cannot find this id'
                break
        print '-'*20
    elif searchInfo == 'age':
        searchAge = input('please input the age : ')
        print '-'*20
        for temp in Tempstudents:
            #for searchName in temp.get('name'):
            if temp.get('age') == searchAge:
                print ' Name is %s ,id is %s,age is %s'%(temp['name'],temp['id'],temp['age'])
                break
            else:
                print 'cannot find this name'
                break
        print '-'*20

#define a list to restor the students information
students = []

while True:
	

#1.0 show the feature list to users
    showInfo()

#1.1 notice the user choose feature
#1.2 get the feature user choosed
    key = int(raw_input('please choose the feature(order number) : '))


#1.3 according to users chooses to execute the equivalent feature
    if key == 1:
        addNewStu(students)
    elif key == 2:
        delStuInfo(students)
    elif key == 3:
        mendStuInfo(students)
    elif key == 4:
        searchStuInfo(students)
    elif key == 5:
        delStuInfo(students)
    elif key == 6:
        quitConfirm=raw_input('honey,u really want to quit>>??<<~~~~~~ [Y/N]')
        if quitConfirm == 'Y' or 'y':
            break
    else:
        print 'Sorry,input the wrong number.'
dent information'
	print '6.quit the system'
	print '-'*30

def addNewStu(studentsTemp):
    #can add the information
    #stuInfo = {'name':'','id':'','age':''}
    #[{},{}]

    name = raw_input('please input name : ')
    stuId = input('please input stuId : ')
    age = input('please input age : ')

    #have a dict,then it has value and key,then can append	
    stuInfo = {}
    stuInfo['name'] = name
    stuInfo['id'] = stuId
    stuInfo['age'] = age
    studentsTemp.append(stuInfo)


def nestingStu(studentsTemp):
    print '-'*20
    print 'next,will show all the students information'
    print ' id          name            age'
    for temp in studentsTemp:
        print ' %s           %s             %s'%(temp['id'],temp['name'],temp['age'])

def delStuInfo(students):
    delNum = input('please input the order:')

    #students = [{'name':'xiaowang','id':111,'age':18}]
    #del students[0]

    del students[delNum]

def mendStuInfo(students):
    mendNum = input('please input the order : ')
    #students = [{'name':'xiaowang','id':111,'age':18}]
    #for x in students:
    #    x['name'] = 'xiaoli'
    #    x['id'] = 222
    #    x['age'] = 12
    #wamt to show the information first , then mend it 
    #for i,n,a in students[menNum]:
    #print ' %s           %s             %s'%(temp['id'],temp['name'],temp['age'])
    mendName = raw_input('please input the new name : ')
    mendId = raw_input('please input the new id : ')
    mendAge = raw_input('please input the new age : ')
        
    #have a dict,then it has value and key,then can mend it
    mendInfo = students[mendNum]
    mendInfo['name'] = mendName
    mendInfo['id'] = mendId
    mendInfo['age'] = mendAge


#define a list to restor the students information
students = []

while True:
	

#1.0 show the feature list to users
    showInfo()

#1.1 notice the user choose feature
#1.2 get the feature user choosed
    key = int(raw_input('please choose the feature(order number) : '))


#1.3 according to users chooses to execute the equivalent feature
    if key == 1:
        addNewStu(students)
    elif key == 2:
        delStuInfo(students)
    elif key == 3:
        mendStuInfo(students)
    elif key == 4:
        #can use the dic ,accordint to the key to situated value..what should i do in the first step.
        #first,let the user choose which key he want to find
        searchInfo = raw_input('please input what is the key you want to use : [name/id/age])



    elif key == 5:
       nestingStu(students) 
    elif key == 6:
        quitConfirm=raw_input('honey,u really want to quit>>??<<~~~~~~ [Y/N]')
        if quitConfirm == 'Y' or 'y':
            break
    else:
        print 'Sorry,input the wrong number.'
