def delete_elem(arr , elem):
	if elem in arr :
		x = arr.index(elem)
		arr.pop(x)
	else:
		print("Element not found ")

list = [12 ,24 ,45]
print(list)

delete_elem(list , 12)
print(list)
