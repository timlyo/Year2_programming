from W1_isSubString import Week1
from W2_8Queens import Week2
from W3_subleq import SubleqProcessor
from W4_Complexity import Week4
from W5_searching import Week5
from W6_sorting import Week6
from W7_RPN import Week7
from W8_LinkList import Week8
from W12_Tree import *
from W14_AVLTree import AVLNode
from W15_Graphs import Graph
from W17_lambdaFunctor import *


def main():
	weeks = [17]
	#weeks = range(14)

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
		Week4.complexity(2, 20, 100, 2)

		print(Week4.efficientDupeFinder((1, 3, 7, 2, 1)))

	if 5 in weeks:
		print("\n***Week 5 - Searching***")
		print(Week5.divideSearch((1, 2, 3, 4, 5, 6, 7), (1, 3)))

	if 6 in weeks:
		print("\n***Week 6 - Sorting***")

		count = [0]
		runCount = 1000

		for x in range(runCount):
			array = Week6.generateArray("random")  # random, worst
			Week6.quicksort(array, count, "middle")  # random, front, middle

		print("Average steps = " + str(count[0]/runCount) + " over {0} times".format(runCount))

	if 7 in weeks:
		print("\n***Week 7 - RPN***")

		Week7.calculate("3 1 2 + * ")

	if 8 in weeks:
		print("\n***Week 8 - Link List***")

		week8 = Week8()

	if 12 in weeks:
		print("\n***Week 12 - Tree***")

		test()

	if 14 in weeks:
		print("\n***Week 14 - AVL Tree***")
		a = AVLNode(50)
		a = a.insert_full(AVLNode(25))
		a = a.insert_full(AVLNode(10))
		a = a.insert_full(AVLNode(30))
		a = a.insert_full(AVLNode(45))
		a = a.insert_full(AVLNode(75))
		a = a.insert_full(AVLNode(65))
		a = a.insert_full(AVLNode(100))
		a = a.insert_full(AVLNode(120))
		a = a.insert_full(AVLNode(125))
		a = a.insert_full(AVLNode(130))
		a = a.insert_full(AVLNode(140))

		a.deleteFull(75)
		a.dot()

	if 15 in weeks:
		print("\n***Week 15 - Graphs***")

		graph = Graph()
		graph.addNode(5)
		graph.addNode(3)
		graph.addNode(1)
		graph.addEdge(graph.getNode(0), graph.getNode(2))
		graph.addEdge(graph.getNode(0), graph.getNode(1))
		graph.addEdge(graph.getNode(1), graph.getNode(0))
		print(graph)

	if 17 in weeks:
		print("\n***Week 17 - lambda functor***")

		numberThing = NumberThing(50)
		numberThing.draw()
		print("==================")
		numberThing.modify(lambda x: x / 2)
		numberThing.draw()



if __name__ == "__main__":
	main()
