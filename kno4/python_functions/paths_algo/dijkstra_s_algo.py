from queue import PriorityQueue

inf: float = 100000.0


def dijkstra(graph, start_vertex):
    d: dict = {v: float('inf') for v in range(graph.v)}
    d[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = d[neighbor]
                    new_cost = d[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        d[neighbor] = new_cost
    return d


# time complexity of this algorithm being O(|Edges|+|Vertices|log|V|)

