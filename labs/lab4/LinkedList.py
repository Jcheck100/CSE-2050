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
            self._head == item
            self._head.link == None
        else:
            
        pass

    def add_last(self):
        pass

    def remove_last(self):
        pass

    def remove_first(self):
        pass

