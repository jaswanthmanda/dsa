# Bipartite graph
"""
Given an undirected graph with V vertices labeled from 0 to V-1.
The graph is represented using an adjacency list where adj[i] lists all nodes connected to node.
Determine if the graph is bipartite or not.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.
"""
"""
Input: V=4, adj = [[1,3],[0,2],[1,3],[0,2]]
Output: True
Explanation: The given graph is bipartite since, we can partition the nodes into two sets: {0, 2} and {1, 3}.

Input: V=4, adj = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: False
Explanation: The graph is not bipartite. If we attempt to partition the nodes into two sets, we encounter an edge that connects two nodes within the same set, which violates the bipartite property.
"""

"""
Constraints:
- E=number of edges
- 1 ≤ V, E ≤ 104
"""

class Solution:
    def isBipartite(self, V, adj):
