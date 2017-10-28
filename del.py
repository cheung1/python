
collegeName=[['zucc','Qinghua'],['Shenzhen','Zhongshan'],['XISU','Jiaoda']]


for x in collegeName:
	for temp in x :
		print temp
	#print x
	print '=========='




family = ['mother','father','husband','wife']

findName = raw_input('please input the name : ')

findFlag = 0 # 0 not found ,1 been found
for temp in family:

	if findName == temp:
		#print 'been found'
		findFlag = 1
		break
	else:
		#print 'not found'
		findFlag = 0

if findFlag == 1:
	print 'been found'
else:
	print 'not found'

print '-------------------------------'


#i = 0
#while i<len(family):
#	temp = family[i]
#	if 'mother' == temp:
#		print 'been found'
#		break
#	else:
#		print 'not found'
#	i += 1
