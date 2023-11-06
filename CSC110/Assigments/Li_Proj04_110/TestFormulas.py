import unittest
import formulas

class TestFormulas(unittest.TestCase):
  def testcalcDistance(self):
    self.assertEqual(formulas.calcDistance(1, 4, 11, 9), '11.1803')

  def testcalcMidpoint(self):
    self.assertEqual(formulas.calcMidpoint(-2, -1, -8, 6), ('-5.0000', '2.5000'))

  def testcalcRadius(self):
    self.assertEqual(formulas.calcRadius(-3, -4, -5, 2), '6.3246')

if __name__ == "__main__":
  unittest.main()