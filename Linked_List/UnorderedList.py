from Node import Node
class UnorderedList:
	def __init__(self):
		self.head = None
	def is_empty(self):
		return self.head == None
	def add(self, item):
		temp = Node(item)
		temp.set_next(self.head)
		self.head = temp
	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.get_data() == item:
				found = True
			else:
				current = current.get_next()
		return found
list = UnorderedList()

list.add(31)
list.add(77)
list.add(17)
list.add(93)

list.add(26)

list.add(54)

print(list.search(26))