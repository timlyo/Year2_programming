import random


class Week6:
	@staticmethod
	def generateArray(type):
		array = []

		# random data
		if type == "random":
			for num in range(512):
				array.append(random.randint(0, 100))

		#worst case
		if type == "worst":
			for num in range(512):
				array.append(num)

		return array

	@staticmethod
	def quicksort(array, count=[0], pivotPlace="random"):
		if len(array) <= 1:
			return array

		smaller = []
		equals = []
		larger = []

		if pivotPlace == "random":
			pivot = random.randint(0, len(array)-1)
		elif pivotPlace == "middle":
			pivot = len(array)//2
		else:  # front
			pivot = 0

		for entry in array:
			count[0] += 1
			if entry < array[pivot]:
				smaller.append(entry)
			elif entry > array[pivot]:
				larger.append(entry)
			else:
				equals.append(entry)

		return Week6.quicksort(smaller, count, pivotPlace) + equals + Week6.quicksort(larger, count, pivotPlace)
