import heapq

# Minimum time to visit disappearing nodes
"""
There is an undirected graph of n nodes. You are given a 2D array edges,
where edges[i] = [ui, vi, lengthi] describes an edge
between node ui and node vi with a traversal time of lengthi units.

Additionally, you are given an array disappear,
where disappear[i] denotes the time when the node i disappears
from the graph and you won't be able to visit it.

Note that the graph might be disconnected and might contain multiple edges.

Return the array answer, with answer[i] denoting the minimum units
of time required to reach node i from node 0.
If node i is unreachable from node 0 then answer[i] is -1.
"""
"""
Example 1:
Input: n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,1,5]
Output: [0,-1,4]
Explanation:
We are starting our journey from node 0, and our goal is to find the minimum
time required to reach each node before it disappears.
- For node 0, we don't need any time as it is our starting point.
- For node 1, we need at least 2 units of time to traverse edges[0].
  Unfortunately, it disappears at that moment, so we won't be able to visit it.
- For node 2, we need at least 4 units of time to traverse edges[2].

Example 2:
Input: n = 3, edges = [[0,1,2],[1,2,1],[0,2,4]], disappear = [1,3,5]
Output: [0,2,3]
Explanation:
We are starting our journey from node 0, and our goal is to find the minimum
time required to reach each node before it disappears.
- For node 0, we don't need any time as it is the starting point.
- For node 1, we need at least 2 units of time to traverse edges[0].
- For node 2, we need at least 3 units of time to traverse edges[0] and edges[1].


Example 3:
Input: n = 2, edges = [[0,1,1]], disappear = [1,1]
Output: [0,-1]
Explanation:
Exactly when we reach node 1, it disappears.
"""
"""
Constraints:
- 1 <= n <= 5 * 104
- 0 <= edges.length <= 105
- edges[i] == [ui, vi, lengthi]
- 0 <= ui, vi <= n - 1
- 1 <= lengthi <= 105
- disappear.length == n
- 1 <= disappear[i] <= 105
"""


class Solution(object):
    def minimumTime(self, n, edges, disappear):
        """
        :type n: int
        :type edges: List[List[int]]
        :type disappear: List[int]
        :rtype: List[int]
        """
        # build adjlist
        adjlist = {i: [] for i in range(n)}
        for u, v, c in edges:
            adjlist[u].append((v, c))
            adjlist[v].append((u, c))

        def srt(start):
            # vis = set([start])
            dist = [float("inf")] * n
            pq = [(0, start)]
            dist[start] = 0

            while pq:
                tim, node = heapq.heappop(pq)

                if tim > dist[node]:
                    continue

                for nei, nei_cos in adjlist[node]:
                    kas = tim + nei_cos
                    if kas < disappear[nei] and kas < dist[nei]:
                        dist[nei] = kas
                        heapq.heappush(pq, (kas, nei))

            return dist

        ans = srt(0)

        for i in range(n):
            if ans[i] == float("inf"):
                ans[i] = -1

        return ans


s = Solution()

k1 = s.minimumTime(
    3,
    [
        [0, 1, 2],
        [1, 2, 1],
        [0, 2, 4],
    ],
    [
        1,
        1,
        5,
    ],
)

k2 = s.minimumTime(
    3,
    [
        [0, 1, 2],
        [1, 2, 1],
        [0, 2, 4],
    ],
    [
        1,
        3,
        5,
    ],
)

k3 = s.minimumTime(
    2,
    [
        [0, 1, 1],
    ],
    [
        1,
        1,
    ],
)

k4 = s.minimumTime(
    2,
    [],
    [0, 1],
)

print(k1)
print(k2)
print(k3)
print(k4)
