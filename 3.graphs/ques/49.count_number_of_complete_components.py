# Count number of complete components
"""
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.
"""
"""
Example 1:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation:
From the picture above, one can see that all of the components of this graph are complete.

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation:
The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.
"""
"""
Constraints:
- 1 <= n <= 50
- 0 <= edges.length <= n * (n - 1) / 2
- edges[i].length == 2
- 0 <= ai, bi <= n - 1
- ai != bi
- There are no repeated edges.
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
            return

        if self.sizes[ulp_u] < self.sizes[ulp_v]:
            self.parents[ulp_u] = ulp_v
            self.sizes[ulp_v] += self.sizes[ulp_u]
        else:
            self.parents[ulp_v] = ulp_u
            self.sizes[ulp_u] += self.sizes[ulp_v]


class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ds = DisjointSet(n)

        for u, v in edges:
            ds.unionBySizes(u, v)

        # 2. Count nodes per component
        comp_size = {}
        for i in range(n):
            root = ds.findUPar(i)
            comp_size[root] = comp_size.get(root, 0) + 1

        # 3. Count edges per component
        comp_edges = {}
        for u, v in edges:
            root = ds.findUPar(u)
            comp_edges[root] = comp_edges.get(root, 0) + 1

        # Check completeness
        complete = 0
        for root in comp_size:
            k = comp_size[root]
            expected_edges = k * (k - 1) // 2
            actual_edges = comp_edges.get(root, 0)
            if actual_edges == expected_edges:
                complete += 1

        return complete


s = Solution()

k1 = s.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4]])

k2 = s.countCompleteComponents(6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]])

print(k1)
print(k2)
