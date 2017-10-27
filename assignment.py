import random
#default a list to restore the name

teachers=['wang','b','c','d','e','f','g','h']

#default a list to restore the office

office=[[],[],[]]


#put the teachers to each office in random way

for name in teachers:
	i = random.randint(0,len(office)-1)
	office[i].append(name)

#print office
#output the information of teachers in office

x=1
for temp in office:
#	print temp
	print 'office %d'%x
	for teachername in temp:
		print teachername
	x+=1
	print '-----------------------------'
	
