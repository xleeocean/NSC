import unittest
import Li_Proj05_110

class TestFormulas(unittest.TestCase):

  def testRate(self):
    self.assertEqual(Li_Proj05_110.rate(7, 8), 1,
                     "When the difference of two ratings is within 1, rate should equals to 1")
    self.assertEqual(Li_Proj05_110.rate(6, 9), 0.7,
                     "When the difference of two ratings is within 3, rate should equals to 0.7")
    self.assertEqual(Li_Proj05_110.rate(4, 10), 0.4,
                     "When the difference of two ratings is within 6, rate should equals to 0.4")
    self.assertEqual(Li_Proj05_110.rate(3, 10), 0,
                     "When the difference of two ratings is more than 6, rate should equals to 0")

# [0]athletic, [1]foodOut, [2]entertainmentOut, [3]seriousRelationship
# [4]religiosity, [5]religion, [6]politics zeal, [7]political leaning

  def testMatch(self):
    p1 = (1, 10, 6, 8, 10, "buddhism", 6, 8)
    p2 = (10, 10, 6, 8, 10, "buddhism", 6, 8)
    self.assertAlmostEqual(Li_Proj05_110.match(p1, p2), 0.85, delta = 0.01,
                           msg="When rate of athletic is 0, the match should be 0.85" )

    p1 = (6, 1, 6, 8, 10, "buddhism", 6, 8)
    p2 = (6, 10, 6, 8, 10, "buddhism", 6, 8)
    self.assertAlmostEqual(Li_Proj05_110.match(p1, p2), 0.9, delta = 0.01,
                           msg="When rate of foodOut is 0, the match should be 0.9" )

    p1 = (6, 10, 1, 8, 10, "buddhism", 6, 8)
    p2 = (6, 10, 10, 8, 10, "buddhism", 6, 8)
    self.assertAlmostEqual(Li_Proj05_110.match(p1, p2), 0.85, delta = 0.01,
                           msg="When rate of entertainmentOut is 0, the match should be 0.85" )

    p1 = (6, 10, 10, 1, 10, "buddhism", 6, 8)
    p2 = (6, 10, 10, 10, 10, "buddhism", 6, 8)
    self.assertAlmostEqual(Li_Proj05_110.match(p1, p2), 0.8, delta = 0.01,
                           msg="When rate of seriousRelationship is 0, the match should be 0.8")

    p1 = (6, 10, 10, 10, 10, "buddhism", 6, 8)
    p2 = (6, 10, 10, 10, 1, "buddhism", 6, 8)
    self.assertAlmostEqual(Li_Proj05_110.match(p1, p2), 1, delta = 0.01,
                           msg="When either person is rated at 8 or above on religiosity, and their religions matches, the match should be 1")

    p1 = (6, 10, 10, 10, 10, "christian", 6, 8)
    p2 = (6, 10, 10, 10, 1, "buddhism", 6, 8)
    self.assertAlmostEqual(Li_Proj05_110.match(p1, p2), 0.9, delta = 0.01,
                           msg="When either person is rated at 8 or above on religiosity, but their religions does not match, the match should be 0.9")

    p1 = (6, 10, 10, 10, 10, "buddhism", 9, 10)
    p2 = (6, 10, 10, 10, 10, "buddhism", 1, 10)
    self.assertAlmostEqual(Li_Proj05_110.match(p1, p2), 1, delta = 0.01,
                           msg="When either person is rated at 9 or above for politics zeal, and political leaning matches, the match should be 1")

    p1 = (6, 10, 10, 10, 10, "buddhism", 9, 1)
    p2 = (6, 10, 10, 10, 10, "buddhism", 1, 10)
    self.assertAlmostEqual(Li_Proj05_110.match(p1, p2), 0.8, delta = 0.01,
                           msg="When either person is rated at 9 or above for politics zeal, and political leaning rate at 1, the match should be 0.8")

    p1 = (6, 10, 10, 10, 10, "buddhism", 1, 1)
    p2 = (6, 10, 10, 10, 10, "buddhism", 1, 10)
    self.assertAlmostEqual(Li_Proj05_110.match(p1, p2), 1, delta = 0.01,
                           msg="When either person is rated lower than 9 for politics zeal, and political leaning matches, the match should be 1")

if __name__ == "__main__":
  unittest.main()