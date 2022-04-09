def dfs(trees, start, target, path = [], visited = set()):
    path.append(start)
    visited.add(start)
    if start == target:
        return path
    for (neighbour, weight) in trees.m_adj_list[start]:
        if neighbour not in visited:
            result = dfs(trees,neighbour, target, path, visited)
            if result is not None:
                return result
    path.pop()
    return None

