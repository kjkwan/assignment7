"""
Computes and creates a Mandelbrot fractal using Mandelbrot iteration. Saves the image as 
mandelbrot.png to your current directory.
"""

import numpy as np
import matplotlib.pyplot as plt
def problemFourOutput():
	def computeMandelbrotFractal(N_max, some_threshold, xRange, yRange):
		# Question 4a: Constructs a grid of c values
		c = constructCGrid(xRange, yRange)
	
		# Question 4b: Performs Mandelbrot iteration
		z = mandelbrotIteration(c)
	
		# Question 4c: Creates and returns a 2-D boolean 
		# mask indicating which points are in the set
		return createMask(z)

	# Helper function creates and returns a Mandelbrot set of complex numbers 'c' in the form of a grid
	def constructCGrid(xRange, yRange):
		# Sets the interval ranges of x and y and evenly spaces the axes as specified by the function arguments.
		# x and y ranges provided in Assignment 7.
		x = np.linspace(-2, 1, xRange)
		y = np.linspace(-1.5, 1.5, yRange)

		# Creates and returns a 2-D grid of complex numbers 'c' using the 
		# equation provided in Assignment 7.
		return x[:, np.newaxis] + 1j * y[np.newaxis,:]

	# Helper function performs Mandelbrot iteration
	def mandelbrotIteration(c):
		# Iteration algorithm provided in Assignment
		np.seterr(all='ignore')		# Ignores values that are out of bounds 
		z = c
		for v in range(N_max):
			z = z**2 + c
		return z

	# Helper function creates and returns a 2-D boolean mask indicating which points are in the set
	def createMask(z):
		# abs(z) makes an imaginary number an unimaginary number for comparison purposes
		mandelbrotSet = (abs(z) < some_threshold)

		return mandelbrotSet

	"""
	Main
	"""
	N_max = 50
	some_threshold = 50
	xRange = 500
	yRange = 500

	mask = computeMandelbrotFractal(N_max, some_threshold, xRange, yRange)

	# Saves result to an image:
	plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
	plt.gray()
	plt.savefig('mandelbrot.png')


# Adapted from SciPy lectures
