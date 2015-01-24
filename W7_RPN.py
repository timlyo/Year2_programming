

class Week7:
	@staticmethod
	def calculate(input):
		input = str(input).split(" ")
		stack = []
		for item in input:
			if item not in "+-/*":
				stack.append(float(item))
			elif len(stack) >= 2:
				stackIndex = len(stack) - 1
				op1 = stack.pop()
				op2 = stack.pop()
				if item == "+":
					stack.append(op1 + op2)
				elif item == "-":
					stack.append(op1 - op2)
				elif item == "*":
					stack.append(op1 * op2)
				elif item == "/":
					stack.append(op1 / op2)

		print(str(input).replace("[", "").replace("]", "").replace(",", "").replace("'", "") + "=")
		print(str(stack).replace("[", "").replace("]", ""))
