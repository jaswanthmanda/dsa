import heapq

# Minimum time for connected k components
"""
You are given an integer n and an undirected graph with n nodes labeled from 0 to n - 1. This is represented by a 2D array edges,
where edges[i] = [ui, vi, timei] indicates an undirected edge between nodes ui and vi that can be removed at timei.

You are also given an integer k.

Initially, the graph may be connected or disconnected. Your task is to find the minimum time t such that after removing all edges with time <= t,
the graph contains at least k connected components.

Return the minimum time t.

A connected component is a subgraph of a graph in which there exists a path between any two vertices,
and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
"""
"""
Example 1:
Input: n = 2, edges = [[0,1,3]], k = 2
Output: 3
Explanation:
- Initially, there is one connected component {0, 1}.
- At time = 1 or 2, the graph remains unchanged.
- At time = 3, edge [0, 1] is removed, resulting in k = 2 connected components {0}, {1}. Thus, the answer is 3.

Example 2:
Input: n = 3, edges = [[0,1,2],[1,2,4]], k = 3
Output: 4
Explanation:
- Initially, there is one connected component {0, 1, 2}.
- At time = 2, edge [0, 1] is removed, resulting in two connected components {0}, {1, 2}.
- At time = 4, edge [1, 2] is removed, resulting in k = 3 connected components {0}, {1}, {2}. Thus, the answer is 4.


Example 3:
Input: n = 3, edges = [[0,2,5]], k = 2
Output: 0
Explanation:
- Since there are already k = 2 disconnected components {1}, {0, 2}, no edge removal is needed. Thus, the answer is 0.
"""
"""
Constraints:
- 1 <= n <= 105
- 0 <= edges.length <= 105
- edges[i] = [ui, vi, timei]
- 0 <= ui, vi < n
- ui != vi
- 1 <= timei <= 109
- 1 <= k <= n
- There are no duplicate edges.
"""


class DisjointSet:
    def __init__(self, V):
        self.nodes = [i for i in range(V)]
        self.parents = [i for i in range(V)]
        self.sizes = [1 for i in range(V)]

    def findUPar(self, u):
        if u == self.parents[u]:
            return u

        self.parents[u] = self.findUPar(self.parents[u])

        return self.parents[u]

    def unionBySizes(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return None

        if self.sizes[ulp_u] < self.sizes[ulp_v]:
            self.sizes[ulp_v] += self.sizes[ulp_u]
            self.parents[ulp_u] = ulp_v
        else:
            self.sizes[ulp_u] += self.sizes[ulp_u]
            self.parents[ulp_v] = ulp_u


class Solution(object):
    def minTime(self, n, edges, k):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        dsu = DisjointSet(n)

        heap_item = [[-1 * w, (u, v)] for u, v, w in edges]

        t = 0

        def comp_count():
            return len(dsu.)

        while heap_item:
            ngw, kk = heapq.heappop(heap_item)

            x, y = kk

            comp_set.remove(x) 

            if len(comp_set) >= k:
