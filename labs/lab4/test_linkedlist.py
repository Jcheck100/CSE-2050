import unittest
from labs.lab4.linkedlist import LinkedList
from Node import Node


class TestNode(unittest.TestCase):
    def test_node_init(self):
        node = Node("A")
        self.assertEqual(node.item, "A")
        self.assertIsNone(node.link)  # Should default to None

        node2 = Node("B", node)
        self.assertEqual(node2.item, "B")
        self.assertEqual(node2.link, node)

    def test_node_repr(self):
        node = Node("Test")
        self.assertEqual(repr(node), "Node(Test)")


class TestLinkedList(unittest.TestCase):
    def test_empty_initialization(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)
        self.assertIsNone(ll.get_head())
        self.assertIsNone(ll.get_tail())

    def test_add_last(self):
        ll = LinkedList()
        ll.add_last("A")
        self.assertEqual(len(ll), 1)
        self.assertEqual(ll.get_head(), "A")
        self.assertEqual(ll.get_tail(), "A")

        ll.add_last("B")
        self.assertEqual(len(ll), 2)
        self.assertEqual(ll.get_head(), "A")
        self.assertEqual(ll.get_tail(), "B")

    def test_non_empty_initialization(self):
        ll = LinkedList(["X", "Y", "Z"])
        self.assertEqual(len(ll), 3)
        self.assertEqual(ll.get_head(), "X")
        self.assertEqual(ll.get_tail(), "Z")

    def test_add_first(self):
        ll = LinkedList()
        ll.add_first("A")
        self.assertEqual(len(ll), 1)
        self.assertEqual(ll.get_head(), "A")
        self.assertEqual(ll.get_tail(), "A")

        ll.add_first("B")
        self.assertEqual(len(ll), 2)
        self.assertEqual(ll.get_head(), "B")  # B should be the new head
        self.assertEqual(ll.get_tail(), "A")  # A should still be the tail

    def test_remove_first(self):
        ll = LinkedList(["1", "2", "3"])
        self.assertEqual(ll.remove_first(), "1")
        self.assertEqual(len(ll), 2)
        self.assertEqual(ll.get_head(), "2")

        self.assertEqual(ll.remove_first(), "2")
        self.assertEqual(ll.remove_first(), "3")
        self.assertEqual(len(ll), 0)
        self.assertIsNone(ll.get_head())

        with self.assertRaises(RuntimeError):
            ll.remove_first()  # Should raise error when list is empty

    def test_remove_last(self):
        ll = LinkedList(["X", "Y", "Z"])
        self.assertEqual(ll.remove_last(), "Z")
        self.assertEqual(len(ll), 2)
        self.assertEqual(ll.get_tail(), "Y")

        self.assertEqual(ll.remove_last(), "Y")
        self.assertEqual(ll.remove_last(), "X")
        self.assertEqual(len(ll), 0)
        self.assertIsNone(ll.get_tail())

        with self.assertRaises(RuntimeError):
            ll.remove_last()  # Should raise error when list is empty


if __name__ == "__main__":
    unittest.main()
