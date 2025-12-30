import heapq

# Find minimum time to reach last room 1
"""
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time
in seconds after which the room opens and can be moved to.
You start from the room (0, 0) at time t = 0 and can move to an adjacent room.
Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.
"""
"""
Example 1:
Input: moveTime = [[0,4],[4,4]]
Output: 6
Explanation:
The minimum time required is 6 seconds.
- At time t == 4, move from room (0, 0) to room (1, 0) in one second.
- At time t == 5, move from room (1, 0) to room (1, 1) in one second.

Example 2:
Input: moveTime = [[0,0,0],[0,0,0]]
Output: 3
Explanation:
The minimum time required is 3 seconds.
- At time t == 0, move from room (0, 0) to room (1, 0) in one second.
- At time t == 0, move from room (0, 0) to room (1, 0) in one second.
- At time t == 2, move from room (1, 1) to room (1, 2) in one second.


Example 3:
Input: moveTime = [[0,1],[1,2]]
Output: 3
"""
"""
Constraints:
- 2 <= n == moveTime.length <= 50
- 2 <= m == moveTime[i].length <= 50
- 0 <= moveTime[i][j] <= 109
"""


class Solution(object):
    def minTimeToReach(self, moveTime):
        """
        :type moveTime: List[List[int]]
        :rtype: int
        """
        m = len(moveTime)
        n = len(moveTime[0])

        def srt(start_x, start_y):
            pq = [(0, (start_x, start_y))]
            dist = [[float("inf")] * n for _ in range(m)]
            dist[start_x][start_y] = 0

            while pq:
                tim, kk = heapq.heappop(pq)

                x, y = kk

                if dist[x][y] < tim:
                    continue

                vals = [
                    (x - 1, y - 1),
                    (x - 1, y),
                    (x + 1, y),
                    (x, y - 1),
                    (x, y + 1),
                ]

                for u, v in vals:
                    if 0 <= u < m and 0 <= v < n:
                        if x == 0 and y == 0:
                            kas = tim + 1
                        else:
                            kas = tim + 1 + moveTime[x][y]
                        # kas = tim + 1 + moveTime[x][y]
                        if kas < dist[u][v]:
                            dist[u][v] = kas
                            heapq.heappush(pq, (kas, (u, v)))

            return dist[m - 1][n - 1]

        ans = srt(0, 0)
        return ans


s = Solution()

k1 = s.minTimeToReach(
    [
        [0, 4],
        [4, 4],
    ]
)

k2 = s.minTimeToReach(
    [
        [0, 0, 0],
        [0, 0, 0],
    ]
)

k3 = s.minTimeToReach(
    [
        [0, 1],
        [1, 2],
    ]
)

k4 = s.minTimeToReach(
    [
        [15, 58],
        [67, 4],
    ]
)

# 
k5 = s.minTimeToReach(
    [
        [17, 56],
        [97, 80],
    ]
)

print(k1)
print(k2)
print(k3)
print(k4)
print(k5)
