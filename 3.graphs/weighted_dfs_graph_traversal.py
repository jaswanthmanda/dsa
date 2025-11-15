from weighted_graph import WeightedGraph


# weighted graph dfs traversal (main logic)
def dfs(graph: WeightedGraph, start):
    visited = set()
    order = []

    def _dfs(node):
        if node not in visited:
            visited.add(node)
            order.append(node)

            for nei, _ in graph.graph[node]:
                if nei not in visited:
                    _dfs(nei)

    _dfs(start)
    return order


if __name__ == "__main__":
    wg = WeightedGraph()
    wg.add_edge(1, 2, 5)
    wg.add_edge(1, 3, 2)
    wg.add_edge(2, 4, 1)
    wg.add_edge(3, 4, 7)

    print("Adjacency List:", wg.graph)
    print("DFS:", dfs(wg, 1))
