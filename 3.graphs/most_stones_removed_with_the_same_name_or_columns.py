# Most stones removed with same row or column
"""
There are n stones at integer coordinate points on a 2D plane,
with at most one stone per coordinate point. Some stones need to be removed.
A stone can be removed if it shares the same row or the same column as another stone that has not been removed.

Given an array of stones of length n where stones[i] = [xi, yi] represents the location of the ith stone,
return the maximum possible number of stones that can be removed.
"""
"""
Input : n=6, stones = [[0, 0],[ 0, 1], [1, 0],[1, 2],[2, 1],[2, 2]]
Output: 5
Explanation:
One of the many ways to remove 5 stones is to remove the following stones:
[0,0], [1,0], [0,1], [2,1], [1,2]



Input : n = 6, stones = [[0, 0], [0, 2], [1, 3], [3, 1], [3, 2], [4, 3]]
Output: 4
Explanation:
We can remove the following stones: [0,0], [0,2], [1,3], [3,1]
"""
"""
Constraints:
- 1 <= n <=1000
- 0 <= x[i], y[i]<= 104
- No two stones are at same position.
"""


class Disjoinset:
    def __init__(self, V):
        self.nodes = [i for i in range(V)]
        self.parents = [i for i in range(V)]
        self.sizes = [1 for i in range(V)]

    def findUPar(self, node):
        if node == self.parents[node]:
            return node

        self.parents[node] = self.findUPar(self.parents[node])

        return self.parents[node]

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_v == ulp_u:
            return

        if self.sizes[ulp_u] < self.sizes[ulp_v]:
            self.parents[ulp_u] = ulp_v
            self.sizes[ulp_v] += self.sizes[ulp_u]
        else:
            self.parents[ulp_v] = ulp_u
            self.sizes[ulp_u] += self.sizes[ulp_v]


class Solution:
    def maxRemove(self, stones, n):
        grid = [[0] * n for i in range(n)]

        ds = Disjoinset(n * n)

        for row, col in stones:
            grid[row][col] = 1

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue


                for a in range(0, )
                if 0 <= a < n and 0 <= b < n and grid[a][b] == 1:
                        nodeNo = row * n + col
                        adjNodeNo = a * n + b
                        ds.unionBySize(nodeNo, adjNodeNo)