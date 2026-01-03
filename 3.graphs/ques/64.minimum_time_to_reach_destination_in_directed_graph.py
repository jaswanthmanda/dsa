import heapq

# Minimum time to reach destination in directed graph
"""
You are given an integer n and a directed graph with n nodes labeled from 0 to n - 1.
This is represented by a 2D array edges, where edges[i] = [ui, vi, starti, endi] indicates an edge
from node ui to vi that can only be used at any integer time t such that starti <= t <= endi.

You start at node 0 at time 0.

In one unit of time, you can either:

- Wait at your current node without moving, or
- Travel along an outgoing edge from your current node if the current time t satisfies starti <= t <= endi.

Return the minimum time required to reach node n - 1. If it is impossible, return -1.
"""
"""
Example 1:
Input: n = 3, edges = [[0,1,0,1],[1,2,2,5]]
Output: 3
Explaination:
The optimal path is:
- At time t = 0, take the edge (0 → 1) which is available from 0 to 1. You arrive at node 1 at time t = 1, then wait until t = 2.
- At time t = 2, take the edge (1 → 2) which is available from 2 to 5. You arrive at node 2 at time 3.

Hence, the minimum time to reach node 2 is 3.



Example 2:
Input: n = 4, edges = [[0,1,0,3],[1,3,7,8],[0,2,1,5],[2,3,4,7]]
Output: 5
Explanation:
The optimal path is:
- Wait at node 0 until time t = 1, then take the edge (0 → 2) which is available from 1 to 5. You arrive at node 2 at t = 2.
- Wait at node 2 until time t = 4, then take the edge (2 → 3) which is available from 4 to 7. You arrive at node 3 at t = 5.
Hence, the minimum time to reach node 3 is 5.


Example 3:
Input: n = 3, edges = [[1,0,1,3],[1,2,3,5]]
Output: -1
Explanation:
- Since there is no outgoing edge from node 0, it is impossible to reach node 2. Hence, the output is -1.
"""
"""
Constraints:
- 1 <= n <= 105
- 0 <= edges.length <= 105
- edges[i] == [ui, vi, starti, endi]
- 0 <= ui, vi <= n - 1
- ui != vi
- 0 <= starti <= endi <= 109
"""


class Solution(object):
    def minTime(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # build adjlist
        adjlist = {i: [] for i in range(n)}
        for u, v, ini, fin in edges:
            adjlist[u].append((v, ini, fin))

        def srt(start):
            dist = [float("inf")] * n
            pq = [(0, start)]

            dist[start] = 0

            while pq:
                timer, node = heapq.heappop(pq)

                if dist[node] < timer:
                    continue

                for nei, nei_ini_tim, nei_fin_tim in adjlist[node]:
                    start_time = max(timer, nei_ini_tim)

                    if start_time > nei_fin_tim:
                        continue

                    arrival_time = start_time + 1

                    if arrival_time < dist[nei]:
                        dist[nei] = arrival_time
                        heapq.heappush(pq, (arrival_time, nei))

            return dist[n - 1]

        ans = srt(0)

        return ans if ans != float("inf") else -1


s = Solution()

k1 = s.minTime(
    3,
    [
        [0, 1, 0, 1],
        [1, 2, 2, 5],
    ],
)

k2 = s.minTime(
    4,
    [
        [0, 1, 0, 3],
        [1, 3, 7, 8],
        [0, 2, 1, 5],
        [2, 3, 4, 7],
    ],
)

k3 = s.minTime(
    3,
    [
        [1, 0, 1, 3],
        [1, 2, 3, 5],
    ],
)

k4 = s.minTime(
    2,
    [
        [0, 1, 4, 4],
    ],
)

k5 = s.minTime(
    5,
    [
        [2, 1, 1, 14],
        [0, 2, 15, 16],
        [1, 4, 1, 11],
        [1, 4, 4, 25],
        [0, 2, 17, 21],
        [3, 0, 13, 22],
        [3, 2, 15, 18],
        [2, 4, 3, 23],
        [1, 3, 11, 12],
    ],
)

print(k1)
print(k2)
print(k3)
print(k4)
print(k5)
