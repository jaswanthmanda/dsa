# Making a large island
"""
Given an n x n binary matrix grid, it is allowed to change at most one 0 to 1.
A group of connected 1s forms an island,9
where two 1s are connected if they share one of their sides.

Return the size of the largest island in the grid after applying this operation.
"""
"""
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation:
We change any one 0 to 1 and connect two 1s, then we get an island with maximum area = 3.

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation:
The largest island already exists with size 4.
"""
"""
Constraints:
- 1 <= n <= 500
- 0 <= grid[i][j] <= 1
"""


class DisjointSet:
    def __init__(self, V):
        self.nodes = [i for i in range(V)]
        self.parent = [i for i in range(V)]
        self.sizes = [1 for i in range(V)]

    def findUPar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUPar(self.parent[node])

        return self.parent[node]

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        if self.sizes[ulp_u] < self.sizes[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.sizes[ulp_v] += self.sizes[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.sizes[ulp_u] += self.sizes[ulp_v]


class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        ds = DisjointSet(n * n)

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue

                vals = [
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ]

                for adjR, adjC in vals:
                    if 0 <= adjR < n and 0 <= adjC < n and grid[adjR][adjC] == 1:
                        rowPoint = row * n + col
                        connPoint = adjR * n + adjC
                        ds.unionBySize(rowPoint, connPoint)

        mx = 0

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue

                vals = [
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ]

                kempG = set()

                for adjR, adjC in vals:
                    if 0 <= adjR < n and 0 <= adjC < n and grid[adjR][adjC] == 1:
                        adjRowNo = adjR * n + adjC
                        kempG.add(ds.findUPar(adjRowNo))

                sm = 0
                for item in kempG:
                    sm += ds.sizes[item]
                sm += 1
                mx = max(sm, mx)

        for i in range(n * n):
            mx = max(mx, ds.sizes[ds.findUPar(i)])

        return mx


s = Solution()

k1 = s.largestIsland(
    [
        [1, 0],
        [0, 1],
    ]
)

k2 = s.largestIsland(
    [
        [1, 1],
        [1, 1],
    ]
)

print(k1)
print(k2)
