from uweighted_graph import UnweightedGraph


# unweighted graph dfs traversal (main logic)
def dfs(graph: UnweightedGraph, start):
    visited = set([])
    order = []

    def _dfs(node):
        visited.add(node)
        order.append(node)

        for nei in graph.graph[node]:
            if nei not in visited:
                _dfs(nei)

    _dfs(start)
    return order


if __name__ == "__main__":
    g = UnweightedGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)

    print("Adjacency List:", dict(g.graph))
    print("DFS:", dfs(g, 1))
