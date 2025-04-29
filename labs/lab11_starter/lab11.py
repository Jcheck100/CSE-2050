class Graph_ES:
    def __init__(self, V = (), E = ()):
        self.V = set()
        self.E = set()
        for v in V:
            self.V.add(v)
        for e in E:
            for e in E:
                u, v = e
                self.E.add((u, v))

    def __len__(self):
        return len(self.V)
    
    def __iter__(self):
        return iter(self.V)
        

    def add_vertex(self, v):
        self.V.add(v)
        

    def remove_vertex(self, v):
        self.V.remove(v)
        

    def add_edge(self, e):
        u,v = e
        self.E.add((u,v))
        

    def remove_edge(self, e):
        u,v = e
        self.E.remove((u,v))
        

    def _neighbors(self, v):
        return (w for u, w in self.E if u == v)

        
class Graph_AS:
    def __init__(self, V = (), E = ()):
        self.neighbors = {}
        for v in V:
            self.add_vertex(v)
        for e in E:
            self.add_edge(e)

    def __len__(self):
        return len(self.neighbors)
    
    def __iter__(self):
        return iter(self.neighbors)
        

    def add_vertex(self, v):
        self.neighbors[v] = set()

    def remove_vertex(self,v):
        if v in self.neighbors:
            for n in self.neighbors.values():
                n.discard(v)
            del self.neighbors[v]
        

    def add_edge(self, e):
        u,v = e
        if u not in self.neighbors:
            self.add_vertex(u)
        if v not in self.neighbors:
            self.add_vertex(v)
        self.neighbors[u].add(v)
        

    def remove_edge(self, e):
        u,v = e
        self.neighbors[u].remove(v)
        

    def _neighbors(self, v):
        return iter(self.neighbors[v])