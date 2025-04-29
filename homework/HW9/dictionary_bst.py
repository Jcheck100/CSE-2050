class Node:
    def __init__(self, word, meaning):
        """Initializes a node with a word, its meaning, and default children and height."""
        self.word = word
        self.meaning = meaning
        self.left = None
        self.right = None
        self.height = 1


class DictionaryBST:
    def __init__(self, entries=None):
        """Initializes the dictionary BST, optionally inserting initial entries"""
        self.root = None
        if entries:
            for word, meaning in entries.items():
                self.insert(word, meaning)

    def insert(self, word, meaning):
        """Inserts a word and its meaning into the tree, maintaining balance."""
        self.root = self._insert(self.root, word, meaning)

    def _insert(self, node, word, meaning):
        """Recursively inserts a node into the subtree and balances the tree"""
        if not node:
            return Node(word, meaning)

        if word < node.word:
            node.left = self._insert(node.left, word, meaning)
        elif word > node.word:
            node.right = self._insert(node.right, word, meaning)
        else:
            node.meaning = meaning
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1:
            if word < node.left.word:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if word > node.right.word:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

    def search(self, word):
        """Searches for a word and returns its meaning if found, else None"""
        return self._search(self.root, word)

    def _search(self, node, word):
        """Recursively searches for a word in the subtree"""
        if not node:
            return None
        if word == node.word:
            return node.meaning
        elif word < node.word:
            return self._search(node.left, word)
        else:
            return self._search(node.right, word)

    def print_alphabetical(self):
        """Returns all dictionary entries in alphabetical order as a list of tuples"""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        """Recursively performs an in-order traversal and appends nodes to result"""
        if node:
            self._inorder(node.left, result)
            result.append((node.word, node.meaning))
            self._inorder(node.right, result)

    def _get_height(self, node):
        """Returns the height of the given node, or 0 if None"""
        return node.height if node else 0

    def _get_balance(self, node):
        """Calculates and returns the balance factor of the given node"""
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _rotate_left(self, unbalanced_node):
        """Performs a left rotation around the given unbalanced node"""
        new_root = unbalanced_node.right
        left_subtree = new_root.left
        new_root.left = unbalanced_node
        unbalanced_node.right = left_subtree

        unbalanced_node.height = 1 + max(self._get_height(unbalanced_node.left), self._get_height(unbalanced_node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root

    def _rotate_right(self, unbalanced_node):
        """Performs a right rotation around the given unbalanced node."""
        new_root = unbalanced_node.left
        right_subtree = new_root.right
        new_root.right = unbalanced_node
        unbalanced_node.left = right_subtree

        unbalanced_node.height = 1 + max(self._get_height(unbalanced_node.left), self._get_height(unbalanced_node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))

        return new_root