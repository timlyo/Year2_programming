class Week4:
	@staticmethod
	def complexity(m1, m2, k1, k2):
		solved = False
		counter = 0.0
		print(str(m1) + "x+" + str(k1))
		print(str(m2) + "x+" + str(k2))

		if m1 > m2 and k1 > k2 or m2 > m1 and k2 > k1:
			print("Error no possible solution")

		while not solved:
			if m1 * counter + k1 - m2 * counter + k2 > 0:
				counter += 1
			elif m1 + counter - k1 < m2 * counter + k2 < 0:
				counter -= 1
			else:
				print("Critical point = {0}, accurate to 1 place".format(counter))
				solved = True


