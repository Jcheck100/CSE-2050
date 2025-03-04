from Node import Node


class LinkedList:
    def __init__(self, items=None):
        """"""
        self._head = None
        self._len = 0
        self._tail = None

        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        """"""
        return self._len

    def get_head(self):
        """"""
        return self._head.item if self._head else None

    def get_tail(self):
        """"""
        return self._tail.item if self._tail else None

    def add_first(self, item):
        """"""
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.link = self._head
            self._head = new_node
        self._len += 1

    def add_last(self, item):
        """"""
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.link = new_node
            self._tail = new_node
        self._len += 1

    def remove_last(self):
        """"""
        if self._head is None:
            raise RuntimeError("Cannot remove from an empty list")

        removed_item = self._tail.item

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            current = self._head
            while current.link != self._tail:
                current = current.link

            current.link = None
            self._tail = current

        self._len -= 1
        return removed_item

    def remove_first(self):
        """"""
        if self._head is None:
            raise RuntimeError("Cannot remove from an empty list")
        
        removed_item = self._head.item
        
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.link

        self._len -= 1
        return removed_item


