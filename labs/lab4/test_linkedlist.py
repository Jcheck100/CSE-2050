from Node import Node
import unittest

class testNode(unittest.TestCase):
    def testnodeinit(self):
        node1 = Node(1, 3)
        self.assertEqual(node1.item, 1)
        self.assertEqual(node1.link, 3)
    
    def testnoderepr(self):
        node1 = Node(1,3)
        self.assertEqual(repr(node1), f"Node({node1.item})")

if __name__ == '__main__':
    unittest.main()
