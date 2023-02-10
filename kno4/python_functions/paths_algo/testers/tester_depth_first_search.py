import unittest

from paths_algo.classes.class_trees import Trees
from paths_algo.depth_first_search import dfs

class TestProject(unittest.TestCase):

    def test_dfs(self):
        trees = Trees(5, directed=False)
        trees.add_edge(0,1)
        trees.add_edge(0, 2)
        trees.add_edge(1, 3)
        trees.add_edge(2, 3)
        trees.add_edge(3, 4)
        result = dfs(trees,0,3)
        self.assertAlmostEqual(result,[0, 1, 3])





