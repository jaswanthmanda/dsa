import heapq

# Find minimum time to reach last room 2
"""
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.
"""
"""
Example 1:
Input: moveTime = [[0,4],[4,4]]
Output: 7
Explanation:
The minimum time required is 7 seconds.
At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.

Example 2:
Input: moveTime = [[0,0,0,0],[0,0,0,0]]
Output: 6
Explanation:
The minimum time required is 6 seconds.
At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
At time t == 3, move from room (1, 1) to room (1, 2) in one second.
At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.

Example 3:
Input: moveTime = [[0,1],[1,2]]
Output: 4
"""
"""
Constraints:
- 2 <= n == moveTime.length <= 750
- 2 <= m == moveTime[i].length <= 750
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
            dist = [[[float("inf"), float("inf")] for _ in range(n)] for i in range(m)]

            pq = [(0, 0, (start_x, start_y))]

            dist[start_x][start_y][0] = 0
            # dist[start_x][start_y][1] = 0

            while pq:
                tim, curr_step, kk = heapq.heappop(pq)

                x, y = kk

                if dist[x][y][curr_step] < tim:
                    continue

                vals = [
                    (x - 1, y),
                    (x + 1, y),
                    (x, y - 1),
                    (x, y + 1),
                ]

                for u, v in vals:
                    if 0 <= u < m and 0 <= v < n:
                        moveCost = 1 if curr_step == 0 else 2
                        curr_nei_step = 1 - curr_step
                        # moveCost = 2 if curr_step == 2 else 1
                        kas = max(moveTime[u][v], tim) + moveCost
                        if dist[u][v][curr_nei_step] > kas:
                            dist[u][v][curr_nei_step] = kas
                            heapq.heappush(pq, (kas, curr_nei_step, (u, v)))

            return min(dist[m - 1][n - 1])

        ans = srt(0, 0)

        return ans


s = Solution()

k1 = s.minTimeToReach([[0, 4], [4, 4]])

k2 = s.minTimeToReach([[0, 0, 0, 0], [0, 0, 0, 0]])

k3 = s.minTimeToReach([[0, 1], [1, 2]])

print(k1)
print(k2)
print(k3)
