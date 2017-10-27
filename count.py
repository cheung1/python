
comp = ['a','b','c','a','d','1','1']

#1.input the element you want to search
findEle = raw_input('please input the element you want to search : ')


# count the element appeares time

countEle = comp.count(findEle)
#print countEle	


#2. search the element is in or not in the list,and print how many times it appeared in the list


if findEle in comp:

	print 'the element you want to search is %s , and is appeared %d times in the comp'%(findEle,countEle)
else:
	print 'the element you want to search is %s , and is appeared %d times in the comp'%(findEle,countEle)
