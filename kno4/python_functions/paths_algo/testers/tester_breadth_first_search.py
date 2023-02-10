import unittest

from paths_algo.classes.class_trees import Trees
from breadth_first_search import bfs

class TestProject(unittest.TestCase):

    def test_dfs(self):
        trees = Trees(6, directed=False)
        trees.add_edge(0, 1)
        trees.add_edge(0, 2)
        trees.add_edge(0, 3)
        trees.add_edge(0, 4)
        trees.add_edge(1, 2)
        trees.add_edge(2, 3)
        trees.add_edge(2, 5)
        trees.add_edge(3, 4)
        trees.add_edge(3, 5)
        trees.add_edge(4, 5)
        result = []
        result = bfs(trees,0, 5)
        self.assertAlmostEqual(result,[0, 3, 5])





