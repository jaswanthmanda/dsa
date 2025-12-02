# Bridges in graph
"""
Given an undirected connected Graph with V vertices (Numbered from 0 to V-1) and E edges.
An edge is represented [ai, bi] denoting that there is an edge from vertex ai to bi.
An edge is called a bridge if its removal makes some vertex unable to reach another vertex.

Return all bridges in the graph in any order.
"""
"""
Examples:
Input: V = 4, E = [ [0,1],[1,2],[2,0],[1,3] ]
Output: [ [1, 3] ]
Explanation:
The edge [1, 3] is the critical edge because if we remove the edge the graph will be divided into 2 components.


Input: V = 3, E = [[0,1],[1,2],[2,0]]
Result: []
Explanation:
There no bridges in the graph.
"""
"""
Constraints:
- 2 <= V, E <= 104
- 0 <= ai, bi <= V - 1
"""

class Solution:
    def criticalConnections(self, V, E):
