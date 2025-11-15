from collections import deque
from weighted_graph import WeightedGraph


# bfs weighted graph example (main logic)
def bfs(graph: WeightedGraph, start):
    visited = set([start])
    order = []
    q = deque([start])

    while q:
        node = q.popleft()
        order.append(node)

        for nei, weight in graph.graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

    return order


if __name__ == "__main__":
    g = WeightedGraph()
    g.add_edge(1, 2, 5)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 4, 1)
    g.add_edge(3, 4, 7)

    print("Adjacency List:", dict(g.graph))
    print("BFS:", bfs(g, 1))
