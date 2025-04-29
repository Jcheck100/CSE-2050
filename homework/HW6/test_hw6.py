import unittest
from hw6 import bubble_sort, selection_sort, insertion_sort, merge

class SortingTestFactory:
    """This class provides methods to generate test cases for sorting algorithms."""
    def setUp(self, sorting_alg):
        """
        Set up the sorting algorithm for testing.
        Args:
            sorting_alg (function): The sorting algorithm to be tested.
        """
        self.sorting_alg = sorting_alg

    def test_merge(self):
        """ Test case for the merge function to verify that it correctly merges three sorted rows."""
        # Define the sorted rows to test
        matrix = [[1, 4, 7, 10], [2, 5, 8, 11],[3, 6, 9, 12]] 
        # Expected merged result
        expected_merged = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        # Call the merge function
        self.assertEqual(expected_merged, merge(matrix[0],matrix[1],matrix[2]))

    def is_sorted(self, L):
        """ Check if a list is sorted. """
        return all(L[i] <= L[i + 1] for i in range(len(L) - 1))

    def test_empty(self):
        """Test sorting on an empty list."""
        matrix = [[], [], []]
        sorted_list, swaps = self.sorting_alg(matrix)
        self.assertEqual(sorted_list, [])
        self.assertEqual(swaps, 0)

    def test_sorted(self):
        """Test sorting on an already sorted list."""
        matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
        sorted_list, swaps = self.sorting_alg(matrix)
        self.assertTrue(self.is_sorted(sorted_list))
        self.assertEqual(swaps, 0)

    def test_reverse_sorted(self):
        """Test sorting on a reverse-sorted list."""
        matrix = [[5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1]]
        sorted_list, swaps = self.sorting_alg(matrix)
        self.assertTrue(self.is_sorted(sorted_list))
        self.assertGreater(swaps, 0)

    def test_random(self):
        """Test sorting on a random list."""
        matrix = [[10, 3, 5, 2, 8], [7, 15, 1, 9, 12], [4, 6, 13, 11, 14]]
        sorted_list, swaps = self.sorting_alg(matrix)
        self.assertTrue(self.is_sorted(sorted_list))
    

class TestBubble(SortingTestFactory, unittest.TestCase):
    """Test class for the bubble sort algorithm."""

    def setUp(self):
        """Set up the bubble sort algorithm for testing."""
        super().setUp(bubble_sort)


class TestInsertion(SortingTestFactory, unittest.TestCase):
    def setUp(self):
        super().setUp(insertion_sort)

class TestSelection(SortingTestFactory, unittest.TestCase):
    def setUp(self):
        super().setUp(selection_sort)

if __name__ == "__main__":
    unittest.main()
