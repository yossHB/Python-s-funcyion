import unittest

from paths_algo.classes.class_graph import Graph
from python_functions.paths_algo.dijkstra_s_algo import dijkstra

class TestProject(unittest.TestCase):

    def test_dijkstra(self):
        g = Graph(9)
        g.add_edge(0, 1, 4)
        g.add_edge(0, 6, 7)
        g.add_edge(1, 6, 11)
        g.add_edge(1, 7, 20)
        g.add_edge(1, 2, 9)
        g.add_edge(2, 3, 6)
        g.add_edge(2, 4, 2)
        g.add_edge(3, 4, 10)
        g.add_edge(3, 5, 5)
        g.add_edge(4, 5, 15)
        g.add_edge(4, 7, 1)
        g.add_edge(4, 8, 5)
        g.add_edge(5, 8, 12)
        g.add_edge(6, 7, 1)
        g.add_edge(7, 8, 3)
        result = dijkstra(g,0)
        self.assertAlmostEqual(result,{0: 0, 1: 4, 2: 11, 3: 17, 4: 9, 5: 22, 6: 7, 7: 8, 8: 11})


