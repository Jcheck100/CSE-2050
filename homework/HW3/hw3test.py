import unittest
from hw3 import generate_lists, find_common, find_common_efficient, measure_time


class TestFunctions(unittest.TestCase):

    def test_generate_lists(self):
        size = 10
        L1, L2 = generate_lists(size)
        self.assertEqual(len(L1), size)
        self.assertEqual(len(L2), size)
        self.assertTrue(all(isinstance(i, int) for i in L1))
        self.assertTrue(all(isinstance(i, int) for i in L2))

    def test_find_common(self):
        L1 = [1, 2, 3, 4, 5]
        L2 = [4, 5, 6, 7, 8]
        self.assertEqual(find_common(L1, L2), 2)

        L1 = [1, 1, 2, 2]
        L2 = [1, 2]
        self.assertEqual(find_common(L1, L2), 3)

        L1 = [1, 1, 1]
        L2 = [2, 2, 2]
        self.assertEqual(find_common(L1, L2), 0)

    def test_find_common_efficient(self):
        L1 = [1, 2, 3, 4, 5]
        L2 = [4, 5, 6, 7, 8]
        self.assertEqual(find_common_efficient(L1, L2), 2)

        L1 = [1, 1, 2, 2]
        L2 = [1, 2]
        self.assertEqual(find_common_efficient(L1, L2), 3)

        L1 = [1, 1, 1]
        L2 = [2, 2, 2]
        self.assertEqual(find_common_efficient(L1, L2), 0)

    def test_find_common_vs_efficient(self):
        L1 = [1, 2, 3, 4, 5]
        L2 = [4, 5, 6, 7, 8]
        self.assertEqual(find_common(L1, L2), find_common_efficient(L1, L2))

        L1 = [1, 1, 2, 2]
        L2 = [1, 2]
        self.assertEqual(find_common(L1, L2), find_common_efficient(L1, L2))

        L1 = [1, 1, 1]
        L2 = [2, 2, 2]
        self.assertEqual(find_common(L1, L2), find_common_efficient(L1, L2))

    def test_measure_time(self):
        try:
            measure_time()
        except Exception as e:
            self.fail(f"measure_time raised an exception {e} unexpectedly!")


unittest.main()