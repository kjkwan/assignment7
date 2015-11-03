import numpy as np

# Problem 2
class Division:
	a = None
	
	def __init__(self, a):
		self.a = a
	
	# Divides each column of the array given in the argument by array b
	# as specified in problem 2. Returns the result.
	def divideColumns(self):
		b = np.array([1., 5, 10, 15, 20])
		self.a = np.transpose(self.a)
		result = self.a/b

		return result.T








	
