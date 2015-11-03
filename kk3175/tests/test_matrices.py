"""
Unit test for problem two.
"""


import numpy as np
from unittest import TestCase
from problemTwo import Division

class MatrixTest(TestCase):
	
	def test_ProblemTwo(self):
		testA = np.array([1,5,10,15,20]*5).reshape(5,5)
		testHelper = Division(testA)
		testResult = testHelper.divideColumns()
		
		expectedOutput = np.array([1,1,1,1,1]*5).reshape(5,5)

		self.assertEqual(expectedOutput.all(), testResult.all())
