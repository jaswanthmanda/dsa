# Number of islands
from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # m, n
        m = len(grid)
        n = len(grid[0])

        vis = set()

        def bfs(start_i, start_j):
            q = deque([(start_i, start_j)])
            vis.add((start_i, start_j))

            while q:
                node_i, node_j = q.popleft()

                vals = [
                    (node_i - 1, node_j),
                    (node_i + 1, node_j),
                    (node_i, node_j - 1),
                    (node_i, node_j + 1),
                ]

                for nei_node_i, nei_node_j in vals:
                    if 0 <= nei_node_i < m and 0 <= nei_node_j < n:
                        if (nei_node_i, nei_node_j) not in vis and grid[nei_node_i][
                            nei_node_j
                        ] == "1":
                            q.append((nei_node_i, nei_node_j))
                            vis.add((nei_node_i, nei_node_j))

        counter = 0

        for i in range(m):
            for j in range(n):
                if (i, j) not in vis and grid[i][j] == "1":
                    bfs(i, j)
                    counter += 1

        return counter
