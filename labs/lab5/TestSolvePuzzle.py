from solve_puzzle import solve_puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
    def testClockwise(self):
        self.assertTrue(solve_puzzle([1, 1, 1, 1, 0]))

    def testCounterClockwise(self):
        self.assertTrue(solve_puzzle([3, 6, 4, 1, 3, 4, 2, 0]))

    def testMixed(self):
        self.assertTrue(solve_puzzle([2, 4, 1, 2, 3, 0]))

    def testUnsolvable(self):
        self.assertFalse(solve_puzzle([3, 4, 1, 2, 0]))

if __name__ == "__main__":
    unittest.main()