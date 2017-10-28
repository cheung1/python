#define a function to calculate 2 number add results
#in brackets,if has varible,when invoke,you need to put varible
# 1.define a function,contains two parameter
def add2num(i,j):
	sum = i + j
	print '%d = %d + %d '%(sum,i,j)

#2.get numbers from users
num1 = input('please input one number : ')
num2 = input('please input another number : ')

add2num(num1,num2)
#if invoke this function,when define,it has to have varibles in brackets/
#then you need to input the varible to invoke function
add2num(j=100,i=200) # u can adjust the order to the parameters results
#the parameters name need to be in the function,or error

#add2num(10,2534) # the number's position is equivalent with the parameter

#if u dont input varible,the error happens
#add2num()
