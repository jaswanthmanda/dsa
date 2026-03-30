# Number of islands
from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        vis = set()

        def bfs(start_node: tuple):
            q = deque([start_node])
            vis.add(start_node)

            while q:
                node = q.popleft()

                a, b = node

                vals = [
                    (a - 1, b),
                    (a + 1, b),
                    (a, b + 1),
                    (a, b - 1),
                ]

                for x, y in vals:
                    if (
                        0 <= x < n
                        and 0 <= y < n
                        and (x, y) not in vis
                        and grid[x][y] == 1
                    ):
                        q.append((x, y))
                        vis.add((x, y))

            counter = 1
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and (i, j) not in vis:
                        counter += 1
                        bfs((i, j))

            return counter