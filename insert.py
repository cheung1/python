
family = ['mother','father','husband','wife']

# family = []

for x in family:
	print x

print '-----------------------------------'

newName = raw_input('please input the name you want to add : ')

#family.append(newName)
family.insert(0,newName)
for x in family:
	print x
