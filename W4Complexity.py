class Week4:
	@staticmethod
	def complexity(m1, m2, k1, k2):
		solved = False
		counter = 0.0
		print(str(m1) + "x+" + str(k1))
		print(str(m2) + "x+" + str(k2))

		while not solved:
			if Week4.getComplexity(m1, counter, k1) > Week4.getComplexity(m2, counter, k2):
				counter += 1
				# print(counter)
			elif Week4.getComplexity(m1, counter, k1) < Week4.getComplexity(m2, counter, k2):
				counter -= 1
				# print(counter)
			else:
				print("Value:", counter)
				solved = True

	@staticmethod
	def getComplexity(m, n, k):
		return m * n + k
