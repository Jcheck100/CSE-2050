import unittest

from Graph import Graph, AdjacencySetGraph, EdgeSetGraph

class GraphTestFactory:
    graph_class = None 

    def graph_ds(self, V=(), E=()):
        return self.graph_class(V, E)

    def test_graph_construction_empty(self):
        g = self.graph_ds()
        self.assertEqual(len(list(g)), 0)

    def test_graph_construction_with_data(self):
        V = {'A', 'B', 'C'}
        E = {('A', 'B'), ('B', 'C')}
        g = self.graph_ds(V, E)
        self.assertEqual(set(g), V)

    def test_is_connected_simple(self):
        V = {'A', 'B', 'C'}
        E = {('A', 'B'), ('B', 'C')}
        g = self.graph_ds(V, E)
        self.assertTrue(g.is_connected('A', 'C'))
        self.assertFalse(g.is_connected('A', 'Z'))

    def test_is_connected_cycle(self):
        V = {'A', 'B', 'C'}
        E = {('A', 'B'), ('B', 'C'), ('C', 'A')}
        g = self.graph_ds(V, E)
        for u in V:
            for v in V:
                self.assertTrue(g.is_connected(u, v))

    def test_bfs_tree_structure(self):
        V = {'A', 'B', 'C', 'D', 'E'}
        E = {('A', 'B'), ('A', 'C'), ('B', 'D'), ('D', 'E')}
        g = self.graph_ds(V, E)
        tree = g.bfs('A')

        
        expected_dist = {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 3}
        actual_dist = {}

        for v in tree:
            dist = 0
            curr = v
            while tree[curr] is not None:
                curr = tree[curr]
                dist += 1
            actual_dist[v] = dist

        self.assertEqual(expected_dist, actual_dist)

    def test_shortest_path(self):
        V = {'A', 'B', 'C', 'D'}
        E = {('A', 'B'), ('B', 'C'), ('C', 'D')}
        g = self.graph_ds(V, E)

        path = g.shortest_path('A', 'D')
        self.assertEqual(path[0], 'A')
        self.assertEqual(path[-1], 'D')
        self.assertEqual(len(path) - 1, 3)

        for i in range(len(path) - 1):
            self.assertIn(path[i+1], list(g.nbrs(path[i])))

    def test_count_trees(self):
        V = {'A', 'B', 'C', 'D', 'E', 'F'}
        E = {('A', 'B'), ('B', 'C'), ('D', 'E')}
        g = self.graph_ds(V, E)
        trees, count = g.count_trees()

        tree_nodes = [set(tree.keys()) for tree in trees]
        expected_sets = [{'A', 'B', 'C'}, {'D', 'E'}, {'F'}]

        self.assertEqual(count, 3)
        for expected in expected_sets:
            self.assertIn(expected, tree_nodes)


class TestAdjacency(GraphTestFactory, unittest.TestCase):
    graph_class = AdjacencySetGraph


class TestEdge(GraphTestFactory, unittest.TestCase):
    graph_class = EdgeSetGraph


class TestGraphInit(unittest.TestCase):
    def test_graph_init_raises(self):
        with self.assertRaises(NotImplementedError):
            Graph()

if __name__ == "__main__":
    unittest.main()