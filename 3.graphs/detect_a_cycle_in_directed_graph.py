# Detect a cycle in a directed graph
"""
Given a directed graph with V vertices labeled from 0 to V-1.
The graph is represented using an adjacency list where adj[i] lists all nodes connected to node.
Determine if the graph contains any cycles.
"""
"""
Input: V = 6, adj= [ [1], [2, 5], [3], [4], [1], [ ] ]
Output: True
Explanation: The graph contains a cycle: 1 -> 2 -> 3 -> 4 -> 1.
"""
"""
Input: V = 4, adj= [[1,2], [2], [], [0,2]]
Output: False
Explanation:
The graph does not contain a cycle.
"""
"""
Constraints:
- E=number of edges
- 1 ≤ V, E ≤ 104
"""
class Solution:
    def isCyclic(self, N, adj):
