def divide_by_2(n):
	n = n/2
	print(n)
	if n > 1:
		divide_by_2(n)
	
	return n

divide_by_2(100)