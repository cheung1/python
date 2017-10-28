#the function has parameter not has a return value
def menu():

	print '-'*30
	print '     card mangement system V8.8'
	print '1.add card'
	print '2.delete card'
	print '3.change card'
	print '4.search card'
	print '5.read each card'
	print '6.quit the system'
	print '-'*30

#get users' information
#this function does not have a parameter ,but has a return value
def getChoice():
	selectedKey = input('please input order number : ')
	return selectedKey


#the function has parameter not has a return value
def printlistInfo(namelistTemp):
    print '='*20
    for temp in namelistTemp:
        print temp
    print '='*20

namelist = []

i=0
while i<10:

	#notice
	menu()

	#waitting for choose
	key = getChoice()

	if key == 1:
		print 'you choose to add card feature'
		newName = raw_input('plese input your name : ')
		namelist.append(newName)
	elif key == 5:
		printlistInfo(namelist)
	elif key == 3:
		pass
	else:
		print 'the demand is wrong'
