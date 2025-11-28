import heapq

# from collections import deque

# Number of ways to arrive at destination
"""
A city consists of n intersections numbered from 0 to n - 1 with
bi-directional roads between some intersections. The inputs are generated such that one can
reach any intersection from any other intersection and that there is at most one road between any two intersections.


Given an integer n and a 2D integer array ‘roads’ where
roads[i] = [ui, vi, timei] means that there is
a road between intersections ui and vi that takes timei minutes to travel.
Determine the number of ways to travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Since the answer may be large, return it modulo 109 + 7.
"""
"""
Input: n=7, m=10, roads= [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation:
The four ways to get there in 7 minutes (which is the shortest calculated time) are:
- 0 6
- 0 4 6
- 0 1 2 5 6
- 0 1 3 5 6

Input: n=6, m=8, roads= [[0,5,8],[0,2,2],[0,1,1],[1,3,3],[1,2,3],[2,5,6],[3,4,2],[4,5,2]]
Output: 3
Explanation:
The three ways to get there in 8 minutes (which is the shortest calculated time) are:
- 0 5
- 0 2 5
- 0 1 3 4 5
"""
"""
Constraints:
- 1 <= n <= 200
- n - 1 <= roads.length <= n * (n - 1) / 2
- roads[i].length == 3
- 0 <= ui, vi <= n - 1
- 1 <= timei <= 109
- ui != vi
"""


class Solution:
    def countPaths(self, n, roads):
        MOD = (10**9 + 7)

        # build adj
        adj = {i: [] for i in range(n)}

        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        dist = [float("inf")] * n
        ways = [0] * n

        pq = [(0, 0)]
        dist[0] = 0
        ways[0] = 1

        while pq:
            wt, node = heapq.heappop(pq)

            if wt > dist[node]:
                continue

            for nei, nei_wt in adj[node]:
                new_time = wt + nei_wt

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (new_time, nei))
                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD

        return ways[n-1] % MOD


s = Solution()

k1 = s.countPaths(
    7,
    [
        [0, 6, 7],
        [0, 1, 2],
        [1, 2, 3],
        [1, 3, 3],
        [6, 3, 3],
        [3, 5, 1],
        [6, 5, 1],
        [2, 5, 1],
        [0, 4, 5],
        [4, 6, 2],
    ],
)

k2 = s.countPaths(
    6,
    [
        [0, 5, 8],
        [0, 2, 2],
        [0, 1, 1],
        [1, 3, 3],
        [1, 2, 3],
        [2, 5, 6],
        [3, 4, 2],
        [4, 5, 2],
    ],
)

print(k1)
print(k2)
