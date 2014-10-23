"""insert meaningful description here"""


class Week1:
	@staticmethod
	def isSubStringEasyVersion(string1, string2):
		"""sane version"""
		return string2 in string1

	@staticmethod
	def isSubString(string1, string2):
		"""checks if string 1 is a substring of string 2"""
		for i in range(len(string1)):
			if string1[i] == string2[0]:
				for j in range(len(string2)):
					if string1[i + j] != string2[j]:
						break
				else:
					return True
		return False
