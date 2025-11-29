import heapq

# Find the city with the smallest number of neighbors
"""
There are n cities numbered from 0 to n-1.
Given the array edges where edges[i] = [fromi, toi,weighti]
represents a bidirectional and weighted edge between cities fromi and toi,
and given the integer distance Threshold.
Find out a city with the smallest number of cities that are reachable
through some path and whose distance is at most Threshold Distance.


If there are multiple such cities, our answer will be the
city with the greatest number.
"""
"""
Input : N=4, M=4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]],
distanceThreshold = 4

Output: 3

Explanation:
The adjacent cities for each city at a distanceThreshold are =
City 0 →[City 1, City 2]
City 1 →[City 0, City 2, City 3]
City 2 →[City 0, City 1, City 3]
City 3 →[City 1, City 2]
Here, City 0 and City 3 have a minimum number of cities
i.e. 2 within distanceThreshold. So, the result will be the
city with the largest number. So, the answer is City 3.

Input : N=3, M=2, edges = [[0,1,1],[0,2,3]], distanceThreshold = 2
Output: 2
Explanation:
City 0 -> City 1,
City 1 → City 0,
City 2 → no City
Hence, 2 is the answer.
"""
"""
Constraints:
- 1 ≤ n ≤ 100
- 1 <= m <= n*(n-1)/2
- length(edges[i]) == 3
- 0 <= fromi < toi < n
- 1 <= weighti , distanceThreshold <= 104
- All pairs (fromi, toi) are distinct
"""


class Solution:
    def bfs(self, start, adjList, n, distanceThreshold):
        pq = [(0, start)]

        dist = [float("inf") for _ in range(n)]

        dist[start] = 0

        while pq:
            wt, node = heapq.heappop(pq)

            if dist[node] < wt:
                continue

            if wt > distanceThreshold:
                continue

            for nei, nei_wt in adjList[node]:
                kas = wt + nei_wt
                if kas < dist[nei]:
                    dist[nei] = kas
                    heapq.heappush(pq, (kas, nei))

        count = 0
        for i in range(n):
            if i != start:
                if dist[i] <= distanceThreshold:
                    count += 1

        return count

    def findCity(self, n, m, edges, distanceThreshold):
        # build adj matrix
        adjList = {i: [] for i in range(n)}
        for u, v, w in edges:
            adjList[u].append((v, w))
            adjList[v].append((u, w))

        dist_count = [float("inf") for _ in range(n)]
        min_threshold = float("inf")
        for i in range(n):
            coo = self.bfs(i, adjList, n, distanceThreshold)
            if min_threshold > coo:
                min_threshold = coo
            dist_count[i] = coo

        max_item = float("-inf")
        for node_i, item in enumerate(dist_count):
            if item == min_threshold:
                if max_item < node_i:
                    max_item = node_i

        return max_item


s = Solution()

k1 = s.findCity(
    4,
    4,
    [
        [0, 1, 3],
        [1, 2, 1],
        [1, 3, 4],
        [2, 3, 1],
    ],
    4,
)

k2 = s.findCity(
    3,
    2,
    [
        [0, 1, 1],
        [0, 2, 3],
    ],
    2,
)

k3 = s.findCity(
    14,
    11,
    [
        [0, 2, 33],
        [2, 8, 11],
        [13, 4, 16],
        [10, 6, 15],
        [11, 8, 92],
        [0, 7, 20],
        [3, 13, 57],
        [0, 1, 8],
        [6, 4, 40],
        [10, 2, 15],
        [0, 5, 49],
    ],
    860,
)

print(k1)
print(k2)
print(k3)
