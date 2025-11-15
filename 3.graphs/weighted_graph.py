from collections import defaultdict


# weighted graph (directional + non-directional)
class WeightedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w, directed=False):
        """Add a weighted edge between u an v."""
        self.graph[u].append((v, w))
        if not directed:
            self.graph[v].append((u, w))
