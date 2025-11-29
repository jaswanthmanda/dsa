# Find the MST weight
"""
You are given a weighted, undirected, and connected
graph with V vertices numbered from 0 to V-1.

The graph is provided in the form of an adjacency list,
where each entry adj[u] contains a list of pairs [v, w],
representing an edge between vertex u and vertex v with weight w.

Find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph.

A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges
of a connected, edge-weighted
undirected graph that connects all the vertices together,
without any cycles and with the minimum possible total edge weight.

Note : The input to the function in code editor is giving in form of adjacency list.
"""
"""
Input: V = 4, adj = [[[1, 1], [3, 4]], [[0, 1], [2, 2]], [[1, 2], [3, 3]], [[0, 4], [2, 3]]]
Output: 6
Explanation:
Edges included in the MST:
- From node 0 → [1, 1] (weight 1)
- From node 1 → [2, 2] (weight 2)
- From node 2 → [3, 3] (weight 3)
The total MST weight is 1 + 2 + 3 = 6.
These edges connect all vertices (0, 1, 2, 3) with minimum cost.
"""
"""
Input: V = 3, adj = [[[1, 5], [2, 15]], [[0, 5], [2, 10]], [[0, 15], [1, 10]]]
Output: 15
Explanation:
Edges included in the MST:
- From node 0 → [1, 5] (weight 5)
- From node 1 → [2, 10] (weight 10)
The total weight of the MST is 5+10 = 15
"""
"""
Constraints:
- 2 ≤ V ≤ 103
- V-1 ≤ E ≤ 104
- 1 ≤ w ≤ 105
"""
class Solution:
    def spanningTree(self, V, adj):
    