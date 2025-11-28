from typing import List
from collections import deque


# Cheapest flight within K stops
"""
There are n cities and m edges connected by some number of flights. Given an array of 
flights where flights[i] = [ fromi, toi, pricei] indicates that there is a flight from city
fromi to city toi with cost pricei. Given three integers src, dst, and k,
and return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.
"""
"""
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The optimal path with at most 1 stops from city 0 to 3 is marked in red and has cost 100 + 600 = 700.

Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The optimal path with at most 1 stops from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
"""
"""
Constraints:
- 1 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2
- flights[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= pricei <= 104
- There will not be any multiple flights between the two cities.
- 0 <= src, dst, k < n
"""
"""
Custom TestCase:
Input: n = 4, flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dst = 3, k = 1
Output: 6


Input: n = 5, flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], src = 0, dst = 2, K = 2
Output: 7
"""


class Solution:
    def CheapestFlight(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        if src == dst:
            return 0

        # build adj matrix
        adj = {i: [] for i in range(n)}

        for a, b, c in flights:
            adj[a].append((b, c))

        dist = [float('inf') for _ in range(n)]

        # (stops, node, price)
        q = deque([(0, src, 0)])

        while q:
            stops, node, price = q.popleft()

            if stops > K:
                continue

            if dist[dst] < price:
                continue

            for nei, nei_price in adj[node]:
                if dist[nei] > price + nei_price:
                    dist[nei] = price + nei_price
                    q.append((stops + 1, nei, price + nei_price))

        return dist[dst] if dist[dst] != float('inf') else -1

s = Solution()

k1 = s.CheapestFlight(
    4,
    [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 100],
        [1, 3, 600],
        [2, 3, 200],
    ],
    0,
    3,
    1,
)

k2 = s.CheapestFlight(
    3,
    [
        [0, 1, 100],
        [1, 2, 100],
        [0, 2, 500],
    ],
    0,
    2,
    1,
)

k3 = s.CheapestFlight(
    4,
    [
        [0, 1, 1],
        [0, 2, 5],
        [1, 2, 1],
        [2, 3, 1],
    ],
    0,
    3,
    1,
)

k4 = s.CheapestFlight(
    5,
    [
        [0, 1, 5],
        [1, 2, 5],
        [0, 3, 2],
        [3, 1, 2],
        [1, 4, 1],
        [4, 2, 1],
    ],
    0,
    2,
    2,
)

print(k1)
print(k2)
print(k3)
print(k4)
