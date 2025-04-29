class Entry():
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def __lt__(self, other): return self.priority < other.priority
    
    def __eq__(self, other): return self.priority == other.priority and self.item == other.item

class PQ_UL():
    def __init__(self):
        self.L = []    
    
    def __len__(self): return len(self.L)

    def insert(self, item, prio):
        self.L.append(Entry(item, prio))
        pass

    def find_min(self):
        if not self.L: return None
        else:
            min_entry = self.L[0]
            for i in range(1, len(self.L)):
                if self.L[i] < min_entry:
                    min_entry = self.L[i]
        return min_entry

    def remove_min(self):
        min_entry = self.find_min()
        if min_entry is not None: 
            self.L.remove(min_entry)
        return min_entry
        

class PQ_OL():
    def __init__(self):
        self.L = []    
    
    def __len__(self): return len(self.L)

    def insert(self, item, prio):
        self.L.append(Entry(item, prio))
        self.L.sort()
        

    def find_min(self):
        if not self.L:
            return None
        return self.L[0]

    def remove_min(self):
        if not self.L:
            return None
        return self.L.pop(0)
