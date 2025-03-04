from process import Process
import unittest

class TestProcess(unittest.TestCase):
    def setUp(self):
        self.p1 = Process(1, 200)
        self.p2 = Process(2)
        self.p3 = Process(1, 300)

    def test_init(self):
        self.assertEqual(self.p1.pid, 1)
        self.assertEqual(self.p1.cycles, 200)
        self.assertIsNone(self.p1.link)
        self.assertIsNone(self.p1.prev)
        
        self.assertEqual(self.p2.pid, 2)
        self.assertEqual(self.p2.cycles, 100)  # Default cycles

    def test_eq(self):
        self.assertEqual(self.p1, self.p3)  # Same pid
        self.assertNotEqual(self.p1, self.p2)  # Different pid
        self.assertNotEqual(self.p1, 100)  # Different type

    def test_repr(self):
        self.assertEqual(repr(self.p1), "1 200")
        self.assertEqual(repr(self.p2), "2 100")

if __name__ == "__main__":
    unittest.main()
