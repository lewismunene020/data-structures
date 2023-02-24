import random as rand

class Task :
	def __init__(self , time) :
		self.time_stamp = time
		self.pages = rand.randrange(1 , 21)

	def get_stamp(self):
		return self.time_stamp()

	def get_pages(self) :
		return self.pages 

	def wait_time(self , current_time ):
		return current_time - self.time_stamp












