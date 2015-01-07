def test():
	file = open("data.csv")
	for line in file:
		formattedLine = line.strip().split("|")
		if formattedLine[0] == "Name":  # if first line
			continue

	file.close()

	baseNode = Node(5)
	baseNode.addLeftChild(Node(10))
	baseNode.addRightChild(Node(8))

	baseNode.print()


class Record:
	def __init__(self, name, address, accountNum, email):
		self.name = name
		self.address = address
		self.accountNUm = accountNum
		self.email = email


class Node:
	def __init__(self, data, parent=None, children=None):
		assert isinstance(children, list) or children is None, type(children)

		self.parent = parent
		self.data = data

		if children is not None:
			self.left = children[0]
			self.right = children[1]
		else:
			self.left = None
			self.right = None

	def addLeftChild(self, node):
		assert isinstance(node, Node)
		self.left = node
		self.left.parent = self

	def addRightChild(self, node):
		assert isinstance(node, Node)
		self.right = node
		self.right.parent = self

	def deleteChild(self, num):
		assert num <= 2
		self.children[num] = None

	def print(self):
		print(self.data)
		if isinstance(self.left, Node):
			self.left.print()
		if isinstance(self.right, Node):
			self.right.print()
