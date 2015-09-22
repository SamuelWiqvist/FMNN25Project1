import unittest
import numpy as np
import spline

class TestEverything(unittest.TestCase):
	def setUp(self):
		self.grid = np.linspace(0, 1, 10)
		self.control_points = np.array([ [1, 2, 1, 4, 5, 5, 7], [1, 0, 3, 4, 5, 1, 3] ])
		self.s = spline.Spline(self.grid, self.control_points)

	def test_something(self):
		self.assertEqual(1, 1)

	def test_a_third_thing(self):
		self.assertAlmostEqual(3, 3 + 1e-8)

	def test_spline(self):
		self.assertIsNotNone(self.s(0.5))

	def test_exception(self):
		self.assertRaises(SystemExit, self.s, self.grid[1])

if __name__ == '__main__':
	unittest.main()
