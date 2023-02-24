class Stack:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return self.items == []
	def push(self , item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)
	def get_item_by_index(self , index):
		return self.items[index]
	def get_all_items(self):
		return self.items
	def push_with_list(self ,list ):
		for i in range(len(list)):
			self.items.append(list[i])

# s = Stack()

# list =[1 ,3 ,5,67 ,123]
# s.push("Item1")
# s.push("Item2")

# print("Current Stack : ",s.get_all_items())
# s.push_with_list(list)
# print("Current Stack : ",s.get_all_items())

# print(s.get_item_by_index(6))

# print(s.is_empty())
# s.peek()
# print(s.size())
