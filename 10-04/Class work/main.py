class Node:
	def __init__(self, data):
		self.data = data
		self.nextNode = None
		self.preNode = None



obj1 = Node("str")
obj2 = Node(1)
obj3 = Node(2)

obj1.nextNode = obj2
obj2.nextNode = obj3