class BinaryTree:
	# implement init function for initialising the tree by giving the self.root of the tree
	def __init__(self ,r):
		self.r = r
		self.root = [self.r , [] ,[]]
	def binary_tree(self):
		return self.root

	def insert_left(self, new_branch):
		t = self.root.pop(1)
		if len(t) >=1 :     # check this to ensure it works 
			self.root.insert(1 ,[t, new_branch , [] ])
		else:
			self.root.insert(1 ,[new_branch , [] , [] ])
		return self.root

	def insert_right(self, new_branch):
		t = self.root.pop(2)
		if len(t) > 1 :
			self.root.insert(2 , [ t ,new_branch ,[] ])
		else:
			self.root.insert(2 , [new_branch , [] , [] ])
		return self.root

	def get_root_val(self):
		return self.root[0]

	def set_root_val(self , new_value) :
		self.root[0] = new_value

	def get_left_child(self):
		print(self.root[1])
		return self.root[1]

	def get_right_child(self):
		print(self.root[2])
		return self.root[2]

# class implementation 
b = BinaryTree("song1")
# traverse and find an element in alist then 
# try band insert an element at a certain level

b.insert_right("song3")
b.insert_left("song2")
b.insert_left("song4")
b.insert_right("song5")

x = b.binary_tree()
# b.get_left_child()
# b.get_right_child()
print(x)

