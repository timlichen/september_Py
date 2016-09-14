class DLList(object):
	def __init__(self, node):
		self.head = node
		self.tail = node

	def add(self, node):
		node.prev = self.tail
		node.prev.next = node
		self.tail = node
		return self

	def insert(self, node, i):
		x = 0
		targetnode = self.head
		while x < i:
			targetnode = targetnode.next
			x += 1
		node.prev = targetnode.prev
		node.next = targetnode
		targetnode.prev = node
		node.prev.next = node
		return self

	def delete(self, i):
		x = 0
		targetnode = self.head
		while x < i:
			targetnode = targetnode.next
			x += 1
		targetnode.prev.next = targetnode.next
		targetnode.next.prev = targetnode.prev
		return self

	def displayNodes(self, node):
		while node:
			print node.value
			node = node.next

class Node(object):
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None

node0 = Node(0)
go = DLList(node0)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

go.add(node1).add(node2).add(node3).add(node4).insert(node5, 2)
go.delete(4)
go.displayNodes(node0)