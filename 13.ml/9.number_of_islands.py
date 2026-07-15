# Number of islands

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.
"""
from typing import List


class Solution:
    def numIslands(
        self,
        grid: List[List[str]],
    ) -> int:
        # m, n
        m = len(grid)
        n = len(grid[0])

        vis = set()

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0" or (i, j) in vis:
                return

            if grid[i][j] == "1":
                vis.add((i, j))

            vals = [
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1),
            ]

            for nei_i, nei_j in vals:
                dfs(nei_i, nei_j)

            return

        counter = 0

        for ii in range(m):
            for jj in range(n):
                if (ii, jj) not in vis and grid[ii][jj] == "1":
                    # print(ii, jj)
                    dfs(ii, jj)
                    counter += 1

        return counter


"""
TC: O(m * n)
SC: O(m, n)
"""
