

filename=['abc.py','hello.py','world.txt','look.rar']


i=1
print len(filename)
while i <= len(filename):
	#i-=1 dead loop
	tempName = filename[i-1]
	dot1 = tempName.rfind('.')
	print tempName[dot1:]
	i+=1	
