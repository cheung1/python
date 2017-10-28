#cal the add up results from 1~ the specified value 

#define a function
def sum2num(endNum):
	i = 1
	sum = 0
	while i<=endNum:
		sum += i
		i += 1

	return sum


#result = sum2num(100)
#print 'the add up from 1 to 100 is : %d'%result

tempNum = input('please input the number you want to use : ')
result = sum2num(tempNum)
print 'the add up from 1 to %d is : %d'%(tempNum,result)


#def number():
#	i = 1
#	sum = 0
#	while i<=100:
#		sum += i
#		i+=1
#	print sum

#number()
