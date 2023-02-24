def merge_sort(list):
	# print("\nSplitting :" ,list)
	if len(list) > 1:
		mid = len(list) //2

		left_half = list[:mid]
		right_half = list[mid:]
		# print(left_half)
		# print(right_half)
		# print(list)
		print("Left list is :" , left_half)
		print("Right list is :" ,right_half)

		merge_sort(left_half)
		merge_sort(right_half)
		print("\n\nLeft sublist successfully divided\n\n")

		i = 0 
		j = 0
		k = 0
		# print(list)
		while i < len(left_half) and j < len(right_half) :
			if left_half[i] < right_half[j]:
				list[k] = left_half[i]
				i = i+1
			else:
				list[k] = right_half[j]
				j = j+1
			k = k+1
			# print(list)

		while i <len(left_half):
			list[k] = left_half[i]
			i+=1
			k+=1

		while j < len(right_half):
			list[k] =  right_half[j]
			j+=1
			k+=1

	print("Current List : ",list)




list =[4,1,3,2]
merge_sort(list)