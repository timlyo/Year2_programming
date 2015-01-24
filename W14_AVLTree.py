class AVLNode(object):
	def __init__(self, data):
		self.data = data
		self.depth = 1
		self.left = None
		self.right = None

	def checkBalance(self):
		# Returns 0 for balanced tree, -1 for left imbalance by 1, +1 for
		# right imbalance by 1, -2 for left imbalance of 2, etc.
		lsize = rsize = 0
		if self.left != None:
			lsize = self.left.depth
		if self.right != None:
			rsize = self.right.depth
		return rsize - lsize

	# Must return the pointer to the root, because it will change
	def rotateRight(self):

		root = self.left
		self.left = root.right
		root.right = self
		if (root.right != None):
			root.right.fixDepth()
		if (root.left != None):
			root.left.fixDepth()
		root.fixDepth()
		return root

	# Must return the pointer to the root, because it will change
	def rotateLeft(self):
		root = self.right
		self.right = root.left
		root.left = self
		if root.right != None:
			root.right.fixDepth()
		if root.left != None:
			root.left.fixDepth()
		root.fixDepth()
		return root

	def fixDepth(self):
		# After child nodes have been moved and their depths fixed, self
		# is used to fix the depth of self node
		lsize = 0 if self.left == None else self.left.depth
		rsize = 0 if self.right == None else self.right.depth
		self.depth = 1 + max(lsize, rsize)

	def insert_full(self, n):
		root = self
		if n.data < self.data:
			if self.left != None:
				self.left = self.left.insert_full(n)
			else:
				self.left = n
		else:
			if self.right != None:
				self.right = self.right.insert_full(n)
			else:
				self.right = n

		if self.checkBalance() < -1:  #Invalid AVL tree with left-habd too heavy
			if self.left.checkBalance() <= 0:  #single rotation to the right
				root = self.rotateRight()
			else:  #Double rotation (could have been done in fewer lines but less clear
				self.left = self.left.rotateLeft()
				root = self.rotateRight()
		elif self.checkBalance() > 1:  #Invalid AVL tree with left-habd too heavy
			if self.right.checkBalance() >= 0:  #single rotation to the left
				root = self.rotateLeft()
			else:  #Double rotation
				self.right = self.right.rotateRight()
				root = self.rotateLeft()
		root.fixDepth()

		return root

	def dot(self, top=True):

		if top:
			print("  digraph G{\n graph [ordering=\"out\"]")
		print(self.data, " [label=\"", self.data, "(", self.depth, ")\"]")
		if self.left != None:
			print(self.data, "->", self.left.data, ";")
			self.left.dot(False)
		if self.right != None:
			print(self.data, "->", self.right.data, ";")
			self.right.dot(False)
		if top:
			print("}")





