###############################################################################
# init, and repr  are implemented for you. You should implement the other     #
# methods recursively.                                                        #
###############################################################################
class Node:
    """Reucrsively implementes Linked List functionality"""
    def __init__(self, data, link=None):
        """Instantiates a new Node with given data"""
        self.data = data
        self.link = link

    def __repr__(self):
        """Returns string representation of node"""
        return f"Node({self.data})"
    
    def __len__(self):
        """Recursively calculates length of sublist starting at this node"""
        if not self.link:
            return 1
        return 1 + len(self.link)

    def get_tail(self):
        """Recursively finds the data stored in the tail of this sublist"""
        if not self.link:
            return self.data
        return self.link.get_tail()
    
    def add_last(self, data):
        """Recursively adds to end of this sublist"""
        if not self.link:
            self.link = Node(data)
        else:
            self.link.add_last(data)

    def total(self):
        """Recusrively adds all items"""
        if not self.link:
            return self.data
        return self.data + self.link.total()
    
    def remove_last(self):
        """Recursively removes last item in sublist
            Returns a tuple of (new_head, data). The new_head is the
            new head of this sublist after removing the tail.

            OUTPUT
            ------
            new_head, tail_data
                * new_head: Node or None
                    The new link for whatever node called this function
                
                * tail_data: Any
                    The data that was found in the tail node
        """
        if not self.link: 
            return None, self.data
        elif not self.link.link:  
            tail_data = self.link.data
            self.link = None
            return self, tail_data
        else:
            new_head, tail_data = self.link.remove_last()
            self.link = new_head  
            return self, tail_data

    def reverse(self, prev):
        """Recursively reverse list"""
        if not self.link:
            self.link = prev
            return self
        new_head = self.link.reverse(self)
        self.link = prev
        return new_head
