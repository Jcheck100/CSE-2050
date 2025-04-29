class Graph:
    def __init__(self, V = (), E = ()):
        """Raise an error to prevent direct instantiation of the abstract Graph class."""
        raise NotImplementedError("Graph is an abstract base class.")
        
    def is_connected(self, v1, v2):
        """Return True if there is a path from v1 to v2, False otherwise."""
        return v2 in self.bfs(v1)

    def bfs(self, v):
        """Perform a breadth-first search starting from vertex v.

        Returns:
            dict: A BFS tree represented as {vertex: parent}.
        """
        tree = {v: None}
        queue = [v]

        while queue:
            v = queue.pop(0)
            for n in self.nbrs(v):
                if n not in tree:
                    tree[n] = v
                    queue.append(n)
        return tree
        
    def shortest_path(self, v1, v2):
        """Return the shortest path from v1 to v2 as a list of vertices, or None if unreachable.

        Args:
            v1: Starting vertex.
            v2: Target vertex.

        Returns:
            list or None: A list of vertices from v1 to v2, or None if no path exists.
        """
        if v1 == v2:
            return [v1]
        
        tree = self.bfs(v1)
        if v2 not in tree:
            return None

        path = []
        curr = v2
        while curr is not None:
            path.append(curr)
            curr = tree[curr]
        path.reverse()
        return path

    def count_trees(self):
        """Return a list of BFS trees and the total number of disconnected components (trees).

        Returns:
            tuple: (list of BFS trees as dictionaries, count of trees)
        """
        visited = set()
        trees = []

        for v in self:
            if v not in visited:
                tree = self.bfs(v)
                trees.append(tree)
                visited.update(tree.keys())
        return trees, len(trees)


class EdgeSetGraph(Graph):
    def __init__(self, V = (), E = ()):
        """Initialize an edge set graph with vertices V and edges E.

        Each edge is stored as a tuple (u, v), and both directions are added to represent an undirected graph.
        """
        self.V = set()
        self.E = set()
        for v in V:
            self.V.add(v)
        for e in E:
            u, v = e
            self.E.add((u, v))
            self.E.add((v, u))

    def __len__(self):
        """Return the number of vertices in the graph."""
        return len(self.V)
    
    def __iter__(self):
        """Iterate over the vertices in the graph."""
        return iter(self.V)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self.V.add(v)

    def add_edge(self, e):
        """Add an undirected edge to the graph as a pair (u, v)."""
        u, v = e
        self.E.add((u, v))
        self.E.add((v, u))

    def nbrs(self, v):
        """Return an iterator over the neighbors of vertex v."""
        return (w for u, w in self.E if u == v)


class AdjacencySetGraph(Graph):
    def __init__(self, V = (), E = ()):
        """Initialize an adjacency set graph with vertices V and edges E."""
        self.neighbors = {}
        for v in V:
            self.add_vertex(v)
        for e in E:
            u, v = e
            self.add_edge((u, v))

    def __len__(self):
        """Return the number of vertices in the graph."""
        return len(self.neighbors)
    
    def __iter__(self):
        """Iterate over the vertices in the graph."""
        return iter(self.neighbors)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        if v not in self.neighbors:
            self.neighbors[v] = set()

    def add_edge(self, e):
        """Add an undirected edge to the graph as a pair (u, v)."""
        u, v = e
        if u not in self.neighbors:
            self.add_vertex(u)
        if v not in self.neighbors:
            self.add_vertex(v)
        self.neighbors[u].add(v)
        self.neighbors[v].add(u)

    def nbrs(self, v):
        """Return an iterator over the neighbors of vertex v."""
        return iter(self.neighbors[v])
