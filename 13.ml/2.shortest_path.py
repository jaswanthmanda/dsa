# Shortest path
from collections import deque

"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:
- n == grid.length == grid[i].length
- 2 <= n <= 100
- grid[i][j] is either 0 or 1.
- There are exactly two islands in grid.
"""


class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # m, n
        m = len(grid)
        n = len(grid[0])
        vis = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r == m or c == n or grid[r][c] == 0:
                return

            vis.add((r, c))

            vals = [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]

            for nei_i, nei_j in vals:
                if (nei_i, nei_j) not in vis:
                    dfs(nei_i, nei_j)

        def bfs(r, c):
            res, q = 0, deque(vis)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()

                    vals = [
                        (r - 1, c),
                        (r + 1, c),
                        (r, c - 1),
                        (r, c + 1),
                    ]

                    for nei_i, nei_j in vals:
                        if (
                            0 <= nei_i < m
                            and 0 <= nei_j < n
                            and (nei_i, nei_j) not in vis
                        ):
                            if grid[nei_i][nei_j] == 0:
                                q.append((nei_i, nei_j))
                                vis.add((nei_i, nei_j))
                            else:
                                return res

                res += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs(i, j)
