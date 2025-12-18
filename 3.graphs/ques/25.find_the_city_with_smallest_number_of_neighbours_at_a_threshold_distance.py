import heapq

# Find the city with smallest number of neighbours at a threshold distance
"""
There are n cities numbered from 0 to n-1.
Given the array edges where edges[i] = [fromi, toi, weighti]
represents a bidirectional and weighted edge
between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through
some path and whose distance is at most distanceThreshold,
If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal
to the sum of the edges' weights along that path.
"""
"""
Example 1:
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation:
The figure above describes the graph.
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2]
City 1 -> [City 0, City 2, City 3]
City 2 -> [City 0, City 1, City 3]
City 3 -> [City 1, City 2]
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Example 2:
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation:
The figure above describes the graph.
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1]
City 1 -> [City 0, City 4]
City 2 -> [City 3, City 4]
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3]
The city 0 has 1 neighboring city at a distanceThreshold = 2.
"""
"""
Constraints:
- 2 <= n <= 100
- 1 <= edges.length <= n * (n - 1) / 2
- edges[i].length == 3
- 0 <= fromi < toi < n
- 1 <= weighti, distanceThreshold <= 10^4
- All pairs (fromi, toi) are distinct.
"""


class Solution(object):
    def srt(self, start, n, adjlist, distanceThres):
        dist = [float("inf")] * n
        dist[start] = 0
        pq = [(0, start)]

        while pq:
            dis, node = heapq.heappop(pq)

            if dist[node] < dis:
                continue

            if dis > distanceThres:
                continue

            for nei_item in adjlist[node]:
                nei, nei_wt = nei_item
                kas = nei_wt + dis
                if dist[nei] > kas:
                    dist[nei] = kas
                    heapq.heappush(pq, (kas, nei))
                    # if kas <= distanceThres:
                    #     items.add(nei)

        cnt = 0
        for i, item in enumerate(dist):
            if i != start and item <= distanceThres:
                cnt += 1

        return cnt

    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        # build adjlist
        adjList = {i: [] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append((edge[1], edge[2]))
            adjList[edge[1]].append((edge[0], edge[2]))

        min_cnt = float("inf")
        max_item = float("-inf")
        for i in range(n):
            k = self.srt(i, n, adjList, distanceThreshold)
            print(i, k)
            if min_cnt > k:
                min_cnt = k
                max_item = i
            elif min_cnt == k and max_item < i:
                max_item = i

        return max_item


s = Solution()

k1 = s.findTheCity(
    4,
    [
        [0, 1, 3],
        [1, 2, 1],
        [1, 3, 4],
        [2, 3, 1],
    ],
    4,
)

k2 = s.findTheCity(
    5,
    [
        [0, 1, 2],
        [0, 4, 8],
        [1, 2, 3],
        [1, 4, 2],
        [2, 3, 1],
        [3, 4, 1],
    ],
    2,
)

print(k1)
print(k2)
