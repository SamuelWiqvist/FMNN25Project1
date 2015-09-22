import unittest
import numpy as np
import spline

class TestEverything(unittest.TestCase):
	def setUp(self):
		self.grid = np.linspace(0, 1, 10)
		self.control_points = np.array([ [1, 2, 1, 4, 5, 5, 7, 8], [1, 0, 3, 4, 5, 1, 3, 3] ])
		self.s = spline.Spline(self.grid, self.control_points)

	def test_exception(self):
		self.assertRaises(ValueError, self.s, self.grid[1])

	def test_de_boor(self):
		uu = np.linspace(self.grid[3], self.grid[-5])
		for u in uu:
			a = self.s(u)
			b = self.s._sum(u)
			self.assertAlmostEqual(a[0], b[0])
			self.assertAlmostEqual(a[1], b[1])

if __name__ == '__main__':
	unittest.main()
