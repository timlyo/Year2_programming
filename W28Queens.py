import random


class Week2:
	def makeBoard(self, size):
		board = []
		for i in range(size):
			board.append([])
			for j in range(size):
				board[-1].append(False)
		return board

	def displayBoard(self, b):
		divider = ("+---" * len(b)) + "+"

		for row in b:
			print(divider)
			line = "|"
			for piece in row:
				if piece is True:
					line += " X |"
				else:
					line += "   |"
			print(line)

	def setAppend(self, s, i):
		""" Add i to s unless i is already in s """
		if not i in s:
			s.append(i)

	def inBoard(self, p, size):
		""" if point is valid for a board of given size, return True. Else return False """
		if 0 <= p[0] < size and 0 <= p[1] < size:
			return True
		else:
			return False

	def pointShift(self, p, r, c):
		""" Return position of cell r,c away from given point p """
		return (p[0] + r, p[1] + c)

	def appendIfInBounds(self, s, p, size):
		""" If point p is within the bounds of a board of given size, append to s unless it's already there """
		if self.inBoard(p, size):
			self.setAppend(s, p)

	def queenSees(self, pos, size):
		""" Return a list of all squares "In view" of a queen in position pos on a board of size"""
		inView = []
		# Row and column
		for i in range(size):

			# Column
			self.setAppend(inView, (i, pos[1]))
			# Row
			self.setAppend(inView, (pos[0], i))
			# Diagonals
			for r in [-1, 1]:
				for c in [-1, 1]:
					self.appendIfInBounds(inView, self.pointShift(pos, r * i, c * i), size)
				# Take out position of queen so she doesn't see herself...
		if pos in inView:
			inView.remove(pos)
		else:
			raise Exception("This should never happen")
		return inView

	def hasQueen(self, board, points):
		""" Returns True if any of the given points on the given board contain a queen """
		for p in points:
			if board[p[0]][p[1]]:
				return True
		return False

	def cloneBoard(self, b, size):
		c = self.makeBoard(size)  # clone
		for i in range(size):
			for j in range(size):
				c[i][j] = b[i][j]
		return c

	def fillBoardRecursion(self, board, row, size):
		""" Given a board completed to given row, try all possible positions for next row and continue """
		if row == size:
			# Base case
			return board
		else:
			for col in range(size):
				if not self.hasQueen(board, self.queenSees((row, col), size)):
					b = self.cloneBoard(board, size)
					b[row][col] = True
					result = self.fillBoardRecursion(b, row + 1, size)
					if result != False:
						return result
			return False  # Failed at this point, so return False

	def fillBoard(self, size):
		b = self.makeBoard(size)
		result = self.fillBoardRecursion(b, 0, size)
		return result


	def fillBoardRandomStart(self, size):
		b = self.makeBoard(size)
		p = random.randint(0, 7)
		b[0][p] = True
		result = fillBoardRecursion(b, 1, size)
		return result


	def fillBoardNaive(self, size):
		b = self.makeBoard(size)
		for r in range(size):
			for c in range(size):
				if not self.hasQueen(b, self.queenSees((r, c), size)):
					b[r][c] = True
					break
			else:
				break
		return b


if __name__ == '__main__':
	week2 = Week2()
	board = week2.fillBoard(8)
	week2.displayBoard(board)


# Advanced
# Can we prove all board sizes have a solution?`
# Can we speed up the solution?
# Perhaps using masks that exclude options...

