from trib import trib
import unittest
class TestTribonacci(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(trib(1), 0)
        self.assertEqual(trib(2), 0)
        self.assertEqual(trib(3), 1)
    
    def test_small_numbers(self):
        self.assertEqual(trib(4), 1)
        self.assertEqual(trib(5), 2)
        self.assertEqual(trib(6), 4)
        self.assertEqual(trib(7), 7)
    
    def test_larger_numbers(self):
        self.assertEqual(trib(10), 44)
        self.assertEqual(trib(15), 927)
        self.assertEqual(trib(20), 35890)
    
    def test_very_large_number(self):
        self.assertEqual(trib(25), 410744)
        self.assertEqual(trib(30), 29249425)
        self.assertEqual(trib(35), 615693474)
    
if __name__ == "__main__":
    unittest.main()