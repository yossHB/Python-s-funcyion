import unittest

from paths_algo.classes.class_graph_2 import Graph
from paths_algo.A_star_search import a_star_algorithm


class TestProject(unittest.TestCase):

    def test_A_star_search(self):
        adjacency_list = {
            'A': [('B', 1), ('C', 3), ('D', 7)],
            'B': [('D', 5)],
            'C': [('D', 12)]
        }
        graph1 = Graph(adjacency_list)
        result= a_star_algorithm(graph1,'A', 'D')
        self.assertAlmostEqual(result,['A', 'B', 'D'])


