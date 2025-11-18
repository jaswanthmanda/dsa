from collections import deque

# Number of enclaves
"""
Given an N x M binary matrix grid, where 0 represents
a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land
cell or walking off the boundary of the grid.
Find the number of land cells in the grid for which we cannot walk
off the boundary of the grid in any number of moves.

Input: grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
Output: 3

Input: grid = [[0, 0, 0, 1],[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
Output: 3
"""


class Solution:
    def numberOfEnclaves(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            count = 0

            while q:
                a, b = q.popleft()
                if a in [0, m - 1] or b in [0, n - 1]:
                    return (0, False)
                count += 1

                vals = [(a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)]

                for val in vals:
                    c = val[0]
                    d = val[1]
                    if 0 <= c < m and 0 <= d < n and grid[c][d] == 1 and (c, d) not in visited:
                        visited.add((c, d))
                        q.append((c, d))

            return (count, True)

        counter = 0
        for i in range(m):
            for j in range(n):
                if (
                    grid[i][j] == 1
                    and i not in [0, m - 1]
                    and j not in [0, n - 1]
                    and (i, j) not in visited
                ):
                    count_temp, cause = bfs(i, j)
                    # print(count_temp, cause)
                    if cause:
                        counter = count_temp

        return counter


s = Solution()
k1 = s.numberOfEnclaves(
    [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
)

k2 = s.numberOfEnclaves(
    [
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
    ]
)

print(k1)
print(k2)
