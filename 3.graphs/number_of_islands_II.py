# Number of islands II
"""
Given n, m denoting the row and column of the 2D matrix, and an array
A of size k denoting the number of operations.
Matrix elements are 0 if there is water or 1 if there is land.
Originally, the 2D matrix
is all 0 which means there is no land in the matrix.
The array has k operator(s) and each operator has
two integers A[i][0], A[i][1] means that you can
change the cell matrix[A[i][0]][A[i][1]] from sea to island.
Return how many islands are there in the matrix after each operation.

The answer array will be of size k.
"""
"""
Input: n = 4, m = 5, k = 4, A = [[1,1],[0,1],[3,3],[3,4]]
Output: [1, 1, 2, 2]
"""
"""
Input: n = 4, m = 5, k = 12, A = [[0,0],[0,0],[1,1],[1,0],[0,1],[0,3],[1,3],[0,4], [3,2], [2,2],[1,2], [0,2]] 
Output: [1, 1, 2, 1, 1, 2, 2, 2, 3, 3, 1, 1]
"""
"""
Constraints:
- 1 <= n, m <= 1000
- 1 <= k <= 104
- 0 <= A[i][0] < n
- 0 <= A[i][1] < m
"""


class Disjoinset:
    def __init__(self, V):
        self.nodes = [i for i in range(V)]
        self.parent = [i for i in range(V)]
        self.sizes = [1 for _ in range(V)]

    def findUPar(self, node):
        if self.parent[node] == node:
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
    def numOfIslands(self, n, m, A):
        ds = Disjoinset(n * m)
        vis = [[False] * m for i in range(n)]
        cnt = 0
        ans = []
        for operator in A:
            row = operator[0]
            col = operator[1]
            if vis[row][col]:
                ans.append(cnt)
                continue

            vis[row][col] = True
            cnt += 1

            vals = [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]

            for val in vals:
                a, b = val[0], val[1]
                if 0 <= a < n and 0 <= b < m:
                    if vis[a][b]:
                        nodeNo = row * m + col
                        adjRowNo = a * m + b
                        if ds.findUPar(nodeNo) != ds.findUPar(adjRowNo):
                            cnt -= 1
                            ds.unionBySize(nodeNo, adjRowNo)

            ans.append(cnt)

        return ans


s = Solution()

k1 = s.numOfIslands(
    4,
    5,
    [
        [1, 1],
        [0, 1],
        [3, 3],
        [3, 4],
    ],
)

k2 = s.numOfIslands(
    4,
    5,
    [
        [0, 0],
        [0, 0],
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 3],
        [1, 3],
        [0, 4],
        [3, 2],
        [2, 2],
        [1, 2],
        [0, 2],
    ],
)

print(k1)
print(k2)
