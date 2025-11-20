from collections import deque


# Number of distinct islands
"""
You are given a 2D matrix grid of size N × M, where each cell contains either 0 or 1.
Find the number of distinct
islands where a group of connected 1s
(horizontally or vertically) forms an island.
Two islands are considered to be same if and only if
one island is equal to another (not rotated or reflected).
"""

"""
Input: grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1],[0, 0, 0, 1, 1]]
Output: 1
Explanation:
Same colored islands are equal. We have 2 equal islands, so we have only 1 distinct island.


Input: grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1],[1, 1, 0, 1, 1]]
Output: 3
Explanation:
Same colored islands are equal. We have 4 islands, but 2 of them are equal, So we have 3 distinct islands..
"""


class Solution:
    def countDistinctIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        final_set = []
        visited = set()

        def bfs(row, col):
            q = deque([(row, col)])
            visited.add((row, col))
            ii_min = row
            jj_min = col
            ii_max = row
            jj_max = col
            stacss = []

            while q:
                a, b = q.popleft()
                stacss.append((a, b))
                if ii_min > a:
                    ii_min = a
                if ii_max < a:
                    ii_max = a
                if jj_min > b:
                    jj_min = b
                if jj_max < b:
                    jj_max = b

                vals = (
                    (a - 1, b),
                    (a + 1, b),
                    (a, b - 1),
                    (a, b + 1),
                )

                for val in vals:
                    r, c = val[0], val[1]
                    if (
                        0 <= r < m
                        and 0 <= c < n
                        and grid[r][c] == 1
                        and (r, c) not in visited
                    ):
                        visited.add((r, c))
                        q.append((r, c))

            return stacss, ii_min, ii_max, jj_min, jj_max

        def buildGraph(stacsss, iii_min, iii_max, jjj_min, jjj_max):
            if len(stacsss) == 0:
                return

            # print(iii_min, iii_max, jjj_min, jjj_max)

            aa = iii_max - iii_min
            ab = jjj_max - jjj_min

            final_sub_mat = [[0 for _ in range(ab + 1)] for i in range(aa + 1)]

            while stacsss:
                aaa, aab = stacsss.pop()
                final_sub_mat[aaa - iii_min][aab - jjj_min] = 1

            if final_sub_mat not in final_set:
                final_set.append(final_sub_mat)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    stacs, i_min, i_max, j_min, j_max = bfs(i, j)
                    buildGraph(stacs, i_min, i_max, j_min, j_max)

        return len(final_set)


s = Solution()

k1 = s.countDistinctIslands(
    [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
    ]
)

k2 = s.countDistinctIslands(
    [
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1],
    ]
)

print(k1)
print(k2)
