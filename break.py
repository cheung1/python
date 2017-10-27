
i = 0

while i < 5:
	print i

	j = 0
	while j <= i:
		j += 1
		if j == 3:
			continue
		print j
	print '-'*20
	i += 1 


	#break
