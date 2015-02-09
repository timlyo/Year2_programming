import random

class NumberThing:
	def __init__(self, amount):
		self.numbers = [random.uniform(-1, 1) for x in range(amount)]

	def draw(self):
		for number in self.numbers:
			if number > 0:
				print(" " * 10 + "#" * int(number * 10.0))
			elif number < 0:
				print(("#" * int(number * -10.0)).rjust(10))
			else:
				print(".")

	def modify(self, lambdaFunc):
		for index, number in enumerate(self.numbers):
			self.numbers[index] = lambdaFunc(number)

