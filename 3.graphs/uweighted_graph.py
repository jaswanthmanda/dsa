from collections import defaultdict


# unweighted graph (direction + undirectional)
class UnweightedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, directed=False):
        """Add an edge between u and v."""
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)
