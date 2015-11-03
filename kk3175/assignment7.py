"""
Prints the results of DSGA1007 Assignment 7 (NumPy Arrays), problems 1-4.
"""

import numpy as np
from problemOne import problemOneOutput
from problemTwo import Division
from problemThree import problemThreeOutput
from problemFour import problemFourOutput

try:
	# Problem 1
	print "Question 1: \n"
	problemOneOutput()

	# Problem 2
	a = Division(np.arange(25).reshape(5,5))
	print "\nQuestion 2: \n"
	print a.divideColumns()

	# Problem 3
	print "\nQuestion 3: \n"
	problemThreeOutput()

	# Problem 4
	print "\nQuestion 4: See current directory for image 'mandelbrot.png'\n"
	problemFourOutput()

except KeyboardInterrupt:
	print "\n Good bye!"


