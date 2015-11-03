import numpy as np

def problemOneOutput():
	# Q1: Use numpy to create the 2D array specified in the assignment.
	# Credit to Matt Dunn.
	twoDArray = np.arange(1,16).reshape((5,3), order='F')
	print "Question 1, 2-D Array: \n %r \n" % twoDArray

	# Q1a: Generate a new array containing the 2nd and 4th rows.
	secondAndFourthRows = np.vstack((twoDArray[1, :], twoDArray[3, :]))
	print "Question 1a, second and fourth rows: \n %r \n" % secondAndFourthRows

	# Q1b: Generate a new array that contains the 2nd column.
	secondColumn = np.vstack((twoDArray[:, 1]))
	print "Question 1b, second column: \n %r \n" % secondColumn

	# Q1c: Generate a new array that contains all the elements in the rectangular section between 
	# coordinates [1,0] and [3,2]

	rectangularSection = twoDArray[1:4, :]
	print "Question 1c, rectangular section between [1,0] and [3,2]: \n %r \n" % rectangularSection

	# Q1d: Generate a new array that contains only elements with values that are between 3 and 11.
	filteredArray = twoDArray[np.where(np.logical_and(twoDArray > 3, twoDArray < 11))]
	print "Question 1d, elements with values between 3 and 11: \n %r \n" % filteredArray

