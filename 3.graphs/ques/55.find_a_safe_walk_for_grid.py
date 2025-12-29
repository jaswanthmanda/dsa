import heapq

# Find a safe walk for grid
"""
You are given an m x n binary matrix grid and an integer health.

You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.
"""
"""
Example 1:
Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1
Output: true
Explanation:
The final cell can be reached safely by walking along the gray cells below.


Example 2:
Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3
Output: false
Explanation:
A minimum of 4 health points is needed to reach the final cell safely.


Example 3:
Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5
Output: true
Explanation:
The final cell can be reached safely by walking along the gray cells below.

Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.
"""
"""
Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- 2 <= m * n
- 1 <= health <= m + n
- grid[i][j] is either 0 or 1.
"""


class Solution(object):
    def findSafeWalk(self, grid, health):
        """
        :type grid: List[List[int]]
        :type health: int
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])

        def srt(start_x, start_y, health):
            if grid[start_x][start_y] == 1:
                health -= 1

            pq = [(-1 * health, (start_x, start_y))]

            dist = [[float("-inf")] * n for _ in range(m)]

            dist[start_x][start_y] = health

            while pq:
                health_rem, kk = heapq.heappop(pq)

                x, y = kk

                temp_health = -1 * health_rem

                if x == m - 1 and y == n - 1 and temp_health >= 1:
                    return True

                if dist[x][y] > temp_health:
                    continue

                vals = [
                    (x - 1, y),
                    (x + 1, y),
                    (x, y - 1),
                    (x, y + 1),
                ]

                for x_nei, y_nei in vals:
                    if 0 <= x_nei < m and 0 <= y_nei < n:
                        kas = -1 * health_rem
                        if grid[x_nei][y_nei] == 1:
                            kas -= 1
                        if kas >= 1 and dist[x_nei][y_nei] < kas:
                            dist[x_nei][y_nei] = kas
                            heapq.heappush(pq, (-1 * kas, (x_nei, y_nei)))

            return False

        ans = srt(0, 0, health)

        return ans


s = Solution()

k1 = s.findSafeWalk([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1)

k2 = s.findSafeWalk(
    [[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]], 3
)

k3 = s.findSafeWalk([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5)

print(k1)
print(k2)
print(k3)
