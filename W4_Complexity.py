from W6_sorting import Week6


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

	@staticmethod
	def linearSearch(search, array):
		for item in array:
			if item == search:
				return True
		return False

	@staticmethod
	def duplicateFinder(array):
		for i in range(len(array)):             # N
			item = array[i]                     # N
			for j in range(i+1, len(array)):    # N*N
				if item == array[j]:            # N*N
					return True                 # N*N
		return False                            # 1

	@staticmethod
	def efficientDupeFinder(array):
		array = Week6.quicksort(array)              #log N

		for index, item in enumerate(array[:-1]):   #N
			if item == array[index+1]:              #N
				return True                         #N
		return False                                #1
