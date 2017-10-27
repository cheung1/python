

filename=['abc.py','hello.py','world.txt','look.rar']


#for i in range(0,len(filename)):
	#temp1 = filename[i]

for temp in filename:
	dot = temp.rfind('.')

	#temp2 = temp1[dot::] 

	print temp[dot:]

	#i+=1



print '--------------------------------'

i=0
print len(filename)
while i < len(filename):
	tempName = filename[i]
	dot1 = tempName.rfind('.')
	print tempName[dot1:]
	i+=1	
