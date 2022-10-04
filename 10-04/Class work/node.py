class Elem:
	#Узел связного списка
	def __init__(self, item):
		self.nextItem = None
		self.item = item

class Node:
	#Связный список
	def __init__(self):
		self.head = None

	def append(self, newItem):
		newItem = Elem(newItem)
		if self.head is None:
			self.head = newItem
			return
		lastElem = self.head
		while lastElem.nextItem:
			lastElem = lastElem.nextItem
		lastElem.nextItem = newItem

	def __contains__(self, item):
		lastElem = self.head