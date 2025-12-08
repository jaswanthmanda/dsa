from collections import deque

# Cheapest flights within K stops
"""
There are n cities connected by some number of flights. You are given an array flights
where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k,
return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.
"""
"""
Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.


Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 tgit o 2 is marked in red and has cost 500.
"""
"""
Constraints:
- 2 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= pricei <= 104
- 0 <= src, dst, k < n
- src != dst
"""


class Solution(object):
    def srtDis(self, n, adjList, src, dst, k):
        if src == dst:
            return 0

        dist = [float("inf")] * n
        dist[src] = 0

        q = deque([(0, src, 0)])
        while q:
            steps, node, wt = q.popleft()
            # print(steps, node, wt)

            if steps > k:
                continue

            if dist[node] > wt:
                continue

            for nei, nei_wt in adjList[node]:
                kas = wt + nei_wt
                if kas < dist[nei]:
                    dist[nei] = kas
                    q.append((steps + 1, nei, kas))

        return -1 if dist[dst] == float("inf") else dist[dst]

    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        # build adjlist
        adjList = {i: [] for i in range(n)}
        for edge in flights:
            adjList[edge[0]].append((edge[1], edge[2]))

        # print(adjList)

        ans = self.srtDis(n, adjList, src, dst, k)

        return ans


s = Solution()

k1 = s.findCheapestPrice(
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

k2 = s.findCheapestPrice(
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

k3 = s.findCheapestPrice(
    3,
    [
        [0, 1, 100],
        [1, 2, 100],
        [0, 2, 500],
    ],
    0,
    2,
    0,
)

# 300
k4 = s.findCheapestPrice(
    4,
    [
        [0, 1, 100],
        [1, 2, 100],
        [2, 3, 100],
        [0, 3, 500],
    ],
    0,
    3,
    2,
)

# 100
k5 = s.findCheapestPrice(
    3,
    [
        [0, 1, 50],
        [1, 2, 50],
        [0, 2, 200],
    ],
    0,
    2,
    1,
)

# 250
k6 = s.findCheapestPrice(
    3,
    [
        [0, 1, 100],
        [1, 2, 100],
        [0, 2, 250],
    ],
    0,
    2,
    0,
)

# 300
k7 = s.findCheapestPrice(
    4,
    [
        [0, 1, 100],
        [1, 0, 10],
        [1, 2, 100],
        [2, 3, 100],
    ],
    0,
    3,
    2,
)


# 101
k8 = s.findCheapestPrice(
    4,
    [
        [0, 1, 1],
        [1, 2, 1],
        [0, 2, 100],
        [2, 3, 1],
    ],
    0,
    3,
    1,
)

# 0
k9 = s.findCheapestPrice(1, [], 0, 0, 5)

# -1
k10 = s.findCheapestPrice(
    5,
    [
        [0, 1, 10],
        [1, 2, 20],
    ],
    0,
    4,
    10,
)

# 40
k11 = s.findCheapestPrice(
    5,
    [
        [0, 1, 10],
        [1, 2, 10],
        [2, 3, 10],
        [3, 4, 10],
        [0, 4, 1000],
    ],
    0,
    4,
    3,
)

# 7
k12 = s.findCheapestPrice(
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
print(k5)
print(k6)
print(k7)
print(k8)
print(k9)
print(k10)
print(k11)
print(k12)
