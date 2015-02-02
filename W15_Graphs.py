class Graph:
	def __init__(self):
		self.nodes = []

	def __str__(self):
		output = "digraph G{\n"
		for node in self.nodes:
			for connection in node.connections:
				output += "\t" + str(node) + " -> " + str(connection) + ";\n"

		return output + "}"

	def addNode(self, value):
		self.nodes.append(Node(value))

	def addEdge(self, node1, node2, twoWay=False):
		assert isinstance(node1, Node)
		assert isinstance(node2, Node)
		node1.addConnection(node2)
		if twoWay:
			node2.addConnection(node1)

	def getNode(self, index):
		assert 0 <= index < len(self.nodes)
		return self.nodes[index]


class Node:
	def __init__(self, value):
		self.value = value
		self.connections = set()

	def __str__(self):
		return str(self.value)

	def addConnection(self, node):
		assert isinstance(node, Node)
		self.connections.add(node)
