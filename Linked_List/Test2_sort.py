def smallest(arr , i , n , pos):
	pos = i
	small = arr[i]
	for (j=i+1) to n :
		if small > arr[j]:
			small = arr[j]
		pos = j
	return pos
def selection(arr , i , n , pos):
	for i =0 to n-1 :
		pos = smallest(arr , i , n , pos)
		arr[i] , arr[pos] = arr[pos] ,arr[i] 
