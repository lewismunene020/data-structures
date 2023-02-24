list =[]
for i in range(3):
	x = int(input("Enter element"))
	list.append(x)

for i in range(len(list-1)):
	small = list[i]

	
	if small > list[i+1] :
		list[i] , list[i+1] = list[i + 1] , list[i]
	
print(list)