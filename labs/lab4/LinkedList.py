class LinkedList():
    def __init__(self, items):
        self._head = None
        self._len = 0
        self._tail = None
    
    def __len__(self):
        return self._len
    
    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    def add_first(self, item):
        if self._head == None:
            self._head = item
            self._head.link = None
            self._tail.link = None
            self._len += 1
        else:
            item.link = self._head
            self._head = item
            self._len += 1


    def add_last(self, item):
        if self._head == None:
            self._head = item
            self._head.link = None
            self._tail.link = None
            self._len += 1
        else:
            pass
        

    def remove_last(self):
        pass

    def remove_first(self):
        pass

L1 = LinkedList(4)
L1.add_first(1)
L1.add_first(2)
L1.add_first(3)
