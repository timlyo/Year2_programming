import sys


class SubleqProcessor:
	def __init__(self, instructionSet):
		self.pointer = 0  # stores current point of execution
		self.memory = [0 for x in range(256)]  # set all memory to 0

		if len(instructionSet) > 256:  # check for memory overflow
			return -1

		instructionSet = list(map(int, instructionSet.split(" ")))
		for index in range(len(instructionSet)):
			self.memory[index] = instructionSet[index]

		self.exit = False

		while not self.exit:
			self.tick()

	def tick(self):
		if self.pointer >= len(self.memory) - 1:
			print("Reached end of memory")
			self.exit = True
			return
		a = self.memory[self.pointer]
		self.pointer += 1
		b = self.memory[self.pointer]
		self.pointer += 1
		c = self.memory[self.pointer]
		self.pointer += 1

		self.memory[b] = self.memory[b] - self.memory[a]

		if c == -1:
			self.exit = True
		if self.memory[b] <= 0:
			if c != -2:
				self.pointer = self.memory[c]
		if b == -1:
			sys.stdout.write(chr(a))
