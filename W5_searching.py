""" pseudo code
for item in array
	if lowerBound < item < upperBound
		return True
return False

"""

""" complexity = O(n)
n	for item in array
n		if lowerBound < item < upperBound
n			return True
1	return False

"""


""" pseudo code
	divideSearch
		if lowerBound < midValue < upperBound
			return True
		if lowerBound > midValue
			return divideSearch(array[:len(array)/2])
		if upperBound < midValue
			return divideSearch(array[len(array)/2:])
		return False
	"""

class Week5:
	@staticmethod
	def linearSearch(array, range):
		for item in array:
			if range[0] < item < range[1]:
				return True
		return False

	@staticmethod
	def divideSearch(array, range):
		midvalue = array[len(array)//2]
		if range[0] < midvalue < range[1]:
			return True
		if range[0] < midvalue:
			return Week5.divideSearch(array[:len(array)//2], range)
		if range[1] > midvalue:
			return Week5.divideSearch(array[len(array)//2:], range)
