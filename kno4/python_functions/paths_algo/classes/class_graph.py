class Graph:

    # example
    # adjacency_list = {
    #                       0: 0,
    #                       1: 4,
    #                       2: 11,
    #                       3: 17,
    #                       4: 9,
    #                       5: 22,
    #                       6: 7,
    #                       7: 8,
    #                       8: 11
    #                   }

    # Constructor
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    # Add edge to the graph
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
