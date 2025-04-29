class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, head = None):
        self.head = head
        self._len = 0
    
    def Len(self):
        return self._len
    
    def addFirst(self, data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            self.head.next = None
        else:
            new_Node.next = self.head
            self.head = new_Node
        self._len +=1
    
    def addLast(self, data):
        new_Node = Node(data)
        if self.head is None:
            self.head = new_Node
            self.head.next = None
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_Node
        self._len +=1
    
    def delFirst(self):
        if self.head is None:
            raise RuntimeError("Cannot Delete from empty List")
        else:
            self.head = self.head.next
        self._len -=1

    def delLast(self):
        if self.head is None:
            raise RuntimeError("Cannot Delete from empty List")
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
        self._len -=1

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next


L1 = LinkedList()

L1.addFirst(12)
L1.addFirst(1)
L1.addLast(5)
L1.delFirst()
L1.delLast()

L1.printList()


