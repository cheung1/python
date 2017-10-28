
i = 1
times = 0

while i <= 9:
	j = 1
	while j <= i:
		times = i * j
		print('%d*%d=%-2d  '%(j,i,times),end='')
		j += 1
	print('\n')
	i += 1
