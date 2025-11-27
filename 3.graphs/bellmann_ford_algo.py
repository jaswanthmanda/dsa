# Bellman ford algorithm
"""
Given a weighted and directed graph of V vertices and E edges. An edge is represented as [ai, bi, wi],
meaning there is a directed edge from ai to bi having weight wi.
Find the shortest distance of all the vertices from the source vertex S.
If a vertex can't be reached from the S then mark the distance as 109.

If the graph contains a negative cycle then return -1 in a list.
"""
"""
Input : V = 6, Edges = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]], S = 0
Output: 0 5 3 3 1 2
Explanation:
- For node 1, shortest path is 0->1 (distance=5).
- For node 2, shortest path is 0->1->2 (distance=3)
- For node 3, shortest path is 0->1->5->3 (distance=3)
- For node 4, shortest path is 0->1->5->3->4 (distance=1)
- For node 5, shortest path is 0->1->5 (distance=2)

Input : V = 2, Edges = [[0,1,9]], S = 0
Output: 0 9
Explanation:
For node 1, the shortest path is 0->1 (distance=9)
"""

class Solution:
    def bellman_ford(self, V, edges, S):
