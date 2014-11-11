from W1_isSubString import Week1
from W2_8Queens import Week2
from W3_subleq import SubleqProcessor
from W4_Complexity import Week4
from W5_searching import Week5
from W6_sorting import Week6
from W7_RPN import Week7

import random


def main():
	weeks = [7]

	if 1 in weeks:
		print("\n***Week 1 - isSubString***")
		print(Week1.isSubString("tacocat", "cat"))

	if 2 in weeks:
		print("\n***Week 2 - ChessThingy***")
		week2 = Week2()
		board = week2.fillBoard(8)
		week2.displayBoard(board)

	if 3 in weeks:
		print("\n***Week 3 - Subleq***")
		helloWorld = "72 -1 -2 " \
		             "101 -1 -2 " \
		             "108 -1 -2 " \
		             "108 -1 -2 " \
		             "111 -1 -2 " \
		             "32 -1 -2 " \
		             "87 -1 -2 " \
		             "111 -1 -2 " \
		             "114 -1 -2 " \
		             "108 -1 -2 " \
		             "100 -1 -2 " \
		             "33 -1 -2 " \
		             "13 -1 -2 " \
		             "10 -1 -2 " \
		             "100 100 -1"
		processor = SubleqProcessor(helloWorld)

	if 4 in weeks:
		print("\n***Week 4 - Complexity***")
						#m1 m2 k1 k2
		Week4.complexity(2, 4, 4, 2)

	if 5 in weeks:
		print("\n***Week 5 - Searching***")
		print(Week5.divideSearch((1, 2, 3, 4, 5, 6, 7), (1, 3)))

	if 6 in weeks:
		print("\n***Week 6 - Sorting***")

		array = Week6.generateArray("worst")  # random, worst

		count = [0]
		runCount = 500

		for x in range(runCount):
			Week6.quicksort(array, count, "random")  # random, front, middle

		print("Average steps = " + str(count[0]/runCount) + " over {0} steps".format(runCount))

	if 7 in weeks:
		print("\n***Week 7 - RPN***")

		Week7.caluclate("3 1 2 + * ")

if __name__ == "__main__":
	main()
