import unittest
from python_core_exercises import Exercises

class CalculatorTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.exe = Exercises()

	def test_editDistance(self):

		self.assertEqual(self.exe.editDistance("sunday", "saturday", len("sunday"), len("saturday")),3)


if __name__ == '__main__':
    unittest.main()