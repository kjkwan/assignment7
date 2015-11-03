import numpy as np

def problemThreeOutput():
	# Generates a 10 x 3 array of random numbers in the range [0,1)
	a = np.random.random((10,3))
	
	# Picks the number closest to 0.5 in each row by creating an array of indices.
	# Each row in the array contains elements that represent indices; the index value 
	# in the 0th column represents the column location of the element closest to 0.5 
	# in the original array generated. 
	b = abs(a - 0.5)
	b = np.argsort(b)
	
	# Creates an array of the column locations containing the element closest to 0.5.
	b = b[:, 0]
	
	# Uses fancy indexing to extract the numbers closest to 0.5 into a new array.
	result = a[np.arange(10), b]

	print result


