from W1_isSubString import Week1
from W2_8Queens import Week2
from W4_Complexity import Week4
from W3_subleq import SubleqProcessor


def main():
	weeks = [1, 2, 3, 4]

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
		             "100 100 -1"
		processor = SubleqProcessor(helloWorld)

	if 4 in weeks:
		print("\n***Week 4 - Complexity***")
		# m  m  k  k
		Week4.complexity(2, 4, 4, 2)


if __name__ == "__main__":
	main()
