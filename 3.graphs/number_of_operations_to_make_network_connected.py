# Number of operations to make network connected
"""
Given a graph with n vertices and m edges.
The graph is represented by an array Edges,
where Edge[i] = [a, b] indicates an edge between vertices a and b.
One edge can be removed from anywhere and added between any two vertices in one operation.
Find the minimum number of operations that will be required to make the graph connected.
If it is not possible to make the graph connected, return -1.
"""
"""
Input : n = 4, Edge =[ [0, 1], [ 0, 2], [1, 2]]
Output: 1
Explanation:
We need a minimum of 1 operation to make the two components connected.
We can remove the edge (1,2) and add the edge
between node 2 and node 3
"""
"""
Input: n = 9, Edge = [[0,1],[0,2],[0,3],[1,2],[2,3],[4,5],[5,6],[7,8]]
Output: 2
Explanation:
We need a minimum of 2 operations to make the two components connected.
We can remove the edge (0,2) and add the edge
between node 3 and node 4 and we can remove the edge (0,3) and add it between nodes 6 and 8.
"""
"""
Constraints:
- 1 <= n <= 104
- 1 <= Edge.length <= 104
- Edge[i].length == 2
"""


class DisJointSet:
    def __init__(self, V):
        self.nodes = [i for i in range(V)]
        self.parent = [i for i in range(V)]
        self.rank = [1 for _ in range(V)]
        self.size = [1 for _ in range(V)]

    def findUpar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUpar(self.parent[node])

        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return

        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findUpar(u)
        ulp_v = self.findUpar(v)
        if ulp_u == ulp_v:
            return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


class Solution:
    def solve(self, n, Edge):
        ds = DisJointSet(n)
        cntExtras = 0
        for edge in Edge:
            u, v = edge[0], edge[1]
            if ds.findUpar(u) == ds.findUpar(v):
                cntExtras += 1
            else:
                ds.unionBySize(u, v)

        cntC = 0
        for i in range(n):
            if ds.parent[i] == i:
                cntC += 1

        return cntC - 1 if cntExtras >= cntC - 1 else -1


s = Solution()

k1 = s.solve(
    4,
    [
        [0, 1],
        [0, 2],
        [1, 2],
    ],
)

k2 = s.solve(
    9,
    [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 2],
        [2, 3],
        [4, 5],
        [5, 6],
        [7, 8],
    ],
)

print(k1)
print(k2)
