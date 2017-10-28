#three numbers sum
def xxx():
	pass

#1.define a function to sum
def sum3num(a,b,c):
	sum = a+b+c
	#print sum
	return sum

#2.define a function to cal average
def aver3(i,j,k):
	#average = (i+j+k)/3
	average = sum3num(i,j,k)/3
	#print average
	return average


num1 = input('please input the first number : ')
num2 = input('please input the second number : ')
num3 = input('please input the third number : ')
sumnum = sum3num(num1,num2,num3)
averagenum = aver3(num1,num2,num3)
print 'sum = %d  '%sumnum
print 'average = %d '%averagenum


