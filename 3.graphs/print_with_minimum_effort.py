import heapq

# Path with minimum effort
"""
A hiker is preparing for an upcoming hike. Given heights,
a 2D array of size rows x columns,
where heights[row][col] represents the height of the cell (row, col).
The hiker is situated in the top-left cell, (0, 0),
and hopes to travel to the bottom-right cell, (rows-1, columns-1) (i.e.,0-indexed).
He can move up, down, left, or right.
He wishes to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference
in heights between two consecutive cells of the route.
"""
"""
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation:
The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Input: heights = [[1,2,3],[3,8,4],[5,3,5]]

Output: 1
Explanation:
The route of [1,2,3,4,5] has a maximum
absolute difference of 1 in consecutive cells,
which is better than route [1,3,5,3,5].
"""
"""
Constraints:
- rows == heights.length
- columns == heights[i].length
- 1 <= rows, columns <= 100
- 1 <= heights[i][j] <= 106
"""


class Solution:
    def MinimumEffort(self, heights):
        m = len(heights)
        n = len(heights[0])

        dist = [[float("inf") for _ in range(n)] for __ in range(m)]
        # parent = [[None for _ in range(n)] for __ in range(m)]

        pq = [(0, 0, 0)]
        dist[0][0] = 0

        while pq:
            effort, x, y = heapq.heappop(pq)

            if effort > dist[x][y]:
                continue

            vals = [
                (x - 1, y),
                (x + 1, y),
                (x, y - 1),
                (x, y + 1),
            ]

            for nx, ny in vals:
                if 0 <= nx < m and 0 <= ny < n:
                    diff = abs(heights[nx][ny] - heights[x][y])
                    new_effort = max(effort, diff)

                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        # parent[nx][ny] = (x, y)
                        heapq.heappush(pq, (new_effort, nx, ny))

        return dist[m - 1][n - 1]


s = Solution()

k1 = s.MinimumEffort(
    [
        [1, 2, 2],
        [3, 8, 2],
        [5, 3, 5],
    ]
)

k2 = s.MinimumEffort(
    [
        [1, 2, 3],
        [3, 8, 4],
        [5, 3, 5],
    ]
)

print(k1)
print(k2)
