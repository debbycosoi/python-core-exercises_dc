import unittest
from python_core_exercises import Exercises

class CalculatorTests(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		"""
		instantiate our class  (fixture)
		"""
		cls.exe = Exercises()

	def test_exercise1(self):

		self.assertEqual(self.exe.exercise1("P@#yn26at^&i5ve"), (8, 3, 4))


if __name__ == '__main__':
    unittest.main()
