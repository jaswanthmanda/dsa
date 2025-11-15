from collections import deque
from uweighted_graph import UnweightedGraph


# unweighted graph bfs example (main logic)
def bfs(graph: UnweightedGraph, start):
    visited = set([start])
    q = deque([start])
    order = []

    while q:
        node = q.popleft()
        order.append(node)

        for nei in graph.graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

    return order


if __name__ == "__main__":
    g = UnweightedGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)

    print("Adjacency List:", dict(g.graph))
    print("BFS:", bfs(g, 1))
