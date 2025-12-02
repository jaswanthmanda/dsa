# Kosaraju's algorithm
"""
You are given a directed graph with V vertices, numbered from 0 to V - 1, and its adjacency list Adj,
where Adj[i] contains all vertices j such that there is a directed edge from vertex i to vertex j.


Your task is to find the number of strongly connected components (SCCs) in the graph.
"""
"""
Examples:
Input: V=5, Adj=[[2,3],[0],[1],[4],[]]
Output: 3

Input: V=8, Adj=[[1],[2],[0,3],[4],[5,7],[6],[4,7],[]]
Output: 4
"""
"""
Constraints:
- 1 ≤ V ≤ 5000
- 0 ≤ E ≤ (V*(V-1))
- 0 ≤ ai, bi ≤ V-1
"""

class Solution:
    def kosaraju(self, V, adj):
