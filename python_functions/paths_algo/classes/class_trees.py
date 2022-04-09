class Trees:

    # example
    # adjacency_list = {
    # node 0 :  {(3, 1), (4, 1), (1, 1), (2, 1)}
    # node 1 :  {(0, 1), (2, 1)}
    # node 2 :  {(0, 1), (5, 1), (3, 1), (1, 1)}
    # node 3 :  {(0, 1), (5, 1), (4, 1), (2, 1)}
    # node 4 :  {(0, 1), (5, 1), (3, 1)}
    # node 5 :  {(3, 1), (4, 1), (2, 1)}
    # }

    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Directed or Undirected
        self.m_directed = directed

        # Graph representation - Adjacency list
        # the use of a dictionary is to implement an adjacency list
        self.m_adj_list = {node: set() for node in self.m_nodes}

    # Add edge to the graph
    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))
        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))

    # Print the graph representation
    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])

