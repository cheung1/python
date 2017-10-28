#print a horizontal line
#the original code
def printline():
	print '-'*20
printline()

#1. change the old code
def printrow(n):
	i=0
	while i<n:
		print '-'*20
		i+=1
		
	
#rowNum = input('please input the number you want to repeat print row : ')
#printrow(rowNum)

#1.change the old code    is not good ,this function may be invoke in other place,will cause some unpredictable accident

#2.define a new function

def printline():
	print '  *  '
	print ' * * '
	print '* * *'

def printrow(n):
	i=0
	while i<n:
		printline()
		i+=1

rowNum = input('please input the number you want to repeat print row : ')
printrow(rowNum)
