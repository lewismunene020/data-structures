class Queue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self , item ):
		self.items.insert(0 , item)

	def dequeue(self) :
		return self.items.pop()

	def size(self) :
		return len(self.items)

	def queue_from_last(self):
		list =[]
		for i in range(len(self.items)):
			list.append(self.items[i] )
		return list	
	def queue_from_first(self):
		list=[]
		for i in range(len(self.items)) :
			list.append(self.items[len(self.items) -(i+1)])
		return list




q = Queue()
q.enqueue("Giant Server")
q.enqueue("Sattelite")
q.enqueue("National Server")
q.enqueue("Router")
q.enqueue("Home server")
q.enqueue("My Laptop ")
print(q.size())
# print(q.queue_from_last())
# print(q.dequeue())
q.enqueue("Rasberrry PI ")
# print(q.queue_from_last())
print("\n",q.dequeue(),"\n")
# print(q.queue_from_first())


