# Articulation point in graph
"""
Given an undirected graph with V vertices and adjacency list adj. Find all the vertices removing which
q(and edges through it) would increase the number of connected components in the graph.
The graph may be initially disconnected..

Return the vertices in ascending order.
If there are no such vertices then returns a list containing -1.

Note: Indexing is zero-based i.e nodes numbering from (0 to V-1).
There might be loops present in the graph.
"""
"""
Examples:
Input: V = 7, adj=[[1,2,3], [0], [0,3,4,5], [2,0], [2,6], [2,6], [4,5]] 
Output: [0, 2]
Explanation:
If we remove node 0 or node 2, the graph will be divided into 2 or more components.


Input: V = 5, adj=[[1], [0,4], [3,4], [2,4], [1,2,3]] 
Output: [1, 4]
Explanation:
If we remove either node 1 or node 4, the graph breaks into multiple components.
"""
"""
Constraints:
- E= Number of Edges
- 1 ≤ V, E ≤ 104
"""

class Solution:
    def articulationPoints(self, n, adj):
