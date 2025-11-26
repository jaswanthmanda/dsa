import heapq

# Shortest Distance in a Binary Maze
"""
Given an n x m matrix grid where each cell contains either 0 or 1, determine
the shortest distance between a source cell and a destination cell.
You can move to an adjacent cell (up, down, left, or right) if that adjacent cell has a value of 1.
The path can only be created out of cells containing 1.
If the destination cell is not reachable from the source cell, return -1.
"""
"""
Input: grid = [[1, 1, 1, 1],[1, 1, 0, 1],[1, 1, 1, 1],[1, 1, 0, 0],[1, 0, 0, 1]], source = [0, 1], destination = [2, 2]
Output: 3
Explanation:
The shortest path from (0, 1) to (2, 2) is:
Move down to (1, 1)
Move down to (2, 1)
Move right to (2, 2)
Thus, the shortest distance is 3


Input: grid = [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 0],[1, 0, 1, 0, 1]], source = [0, 0], destination = [3, 4]
Output: -1
Explanation:
Since, there is no path possible between the source cell and the destination cell, hence we return -1.
"""


class Solution:
    def shortestPath(self, grid, source, destination):
        m = len(grid)
        n = len(grid[0])

        # ans wt
        ans_wt = [[float("inf") for _ in range(n)] for __ in range(m)]

        pq = [(0, (source[0], source[1]))]
        ans_wt[source[0]][source[1]] = 0
        ii, jj = None, None

        while pq or [ii, jj] == destination:
            wt, source_node = heapq.heappop(pq)
            ii, jj = source_node

            if wt > ans_wt[ii][jj]:
                continue

            vals = [
                (ii - 1, jj),
                (ii + 1, jj),
                (ii, jj - 1),
                (ii, jj + 1),
            ]

            for aa, bb in vals:
                if 0 <= aa < m and 0 <= bb < n:
                    if grid[aa][bb] == 1 and wt + 1 < ans_wt[aa][bb]:
                        ans_wt[aa][bb] = wt + 1
                        heapq.heappush(pq, (wt + 1, (aa, bb)))

        for iii in range(m):
            for jjj in range(n):
                if ans_wt[iii][jjj] == float("inf"):
                    ans_wt[iii][jjj] = -1

        dest_a, dest_b = destination[0], destination[1]
        return ans_wt[dest_a][dest_b]


s = Solution()

k1 = s.shortestPath(
    [
        [1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 0, 1],
    ],
    [0, 1],
    [2, 2],
)

k2 = s.shortestPath(
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 0, 1],
    ],
    [0, 0],
    [3, 4],
)

print(k1)
print(k2)
