class Week8:
	def __init__(self):
		l = List()
		l.insert(None, Node(1))
		l.insert(l.head, Node(4))
		l.insert(l.head, Node(6))
		l.insert(l.head, Node(3))
		l.insert(None, Node(2))
		l.display()
		l.bubbleSort()
		l.display()


class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None


class List(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, back, newNode):
		assert isinstance(back, Node) or back is None, type(back)
		assert isinstance(newNode, Node) or newNode is None, type(newNode)

		if back is not None:
			newNode.next = back.next
			if back.next is not None:  # moved to fix the code
				back.next.prev = newNode
			back.next = newNode
			newNode.prev = back

		elif self.head is not None:  # prepend
			self.head.prev = newNode
			newNode.next = self.head
			self.head = newNode

		if self.head is None:  # if first element
			self.head = self.tail = newNode
			newNode.prev = newNode.next = None
		elif self.tail == back:  # if only 1 element
			self.tail = newNode

	def delete(self, node):
		assert isinstance(node, Node)
		node.prev.next = node.next
		node.next.prev = node.prev

	def display(self):
		values = []
		n = self.head
		while n is not None:
			values.append(str(n.value))
			n = n.next
			if len(values) > 20:
				break
		print("List: ", ",".join(values))

	def displayReversed(self):
		values = []
		n = self.tail
		while n is not None:
			values.append(str(n.value))
			n = n.prev
			if len(values) > 20:
				break
		print("List:", ",".join(values))

	def bubbleSort(self):
		node = self.head
		while True:
			value = node.value
			swapped = False

			if node.next is None:  # if at end
				if not swapped:
					break
				node = self.head

			if node.value > node.next.value:
				self.swapNodes(node, node.next)
				node = self.head
			else:
				node = node.next  # move on

	def swapNodes(self, node1, node2):
		assert isinstance(node1, Node)
		assert isinstance(node2, Node)


		node1.next = node2.next
		node2.next = node1

		node2.prev = node1.prev
		if node1.prev is None:  # if first node
			self.head = node2
		else:
			node1.prev.next = node2

