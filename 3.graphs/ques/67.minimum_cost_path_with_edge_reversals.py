import heapq

# Minimum cost path with edge reversals
"""
You are given a directed, weighted graph with n nodes labeled from 0 to n - 1,
and an array edges where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with cost wi.

Each node ui has a switch that can be used at most once: when you arrive at ui and have not yet used its switch,
you may activate it on one of its incoming edges vi → ui reverse that edge to ui → vi and immediately traverse it.

The reversal is only valid for that single move, and using a reversed edge costs 2 * wi.

Return the minimum total cost to travel from node 0 to node n - 1. If it is not possible, return -1.
"""
"""
Example 1:
Input: n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
Output: 5
Explanation:
- Use the path 0 → 1 (cost 3).
- At node 1 reverse the original edge 3 → 1 into 1 → 3 and traverse it at cost 2 * 1 = 2.
- Total cost is 3 + 2 = 5.

Example 2:
Input: n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]
Output: 3
Explanation:
- No reversal is needed. Take the path 0 → 2 (cost 1), then 2 → 1 (cost 1), then 1 → 3 (cost 1).
- No reversal is needed. Take the path 0 → 2 (cost 1), then 2 → 1 (cost 1), then 1 → 3 (cost 1).
"""
"""
Constraints:
- 2 <= n <= 5 * 104
- 1 <= edges.length <= 105
- edges[i] = [ui, vi, wi]
- 0 <= ui, vi <= n - 1
- 1 <= wi <= 1000
"""


class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # build adjlist
        out_adj = {i: [] for i in range(n)}
        in_adj = {i: [] for i in range(n)}
        for u, v, w in edges:
            out_adj[u].append((v, w))
            in_adj[v].append((u, w))

        dist = [float("inf") for i in range(n)]
        pq = [(0, 0)]

        dist[0] = 0

        while pq:
            t, node = heapq.heappop(pq)

            if dist[node] < t:
                continue

            for nei, nei_wt in out_adj[node]:
                kas = nei_wt + t
                if kas < dist[nei]:
                    dist[nei] = kas
                    heapq.heappush(pq, (kas, nei))

            # Allowed once per node visit
            for nei, nei_wt in in_adj[node]:
                kas = t + (2 * nei_wt)
                if kas < dist[nei]:
                    dist[nei] = kas
                    heapq.heappush(pq, (kas, nei))

        ans = dist[n - 1]

        return ans if ans != float("inf") else -1


s = Solution()

k1 = s.minCost(
    4,
    [
        [0, 1, 3],
        [3, 1, 1],
        [2, 3, 4],
        [0, 2, 2],
    ],
)

k2 = s.minCost(
    4,
    [
        [0, 2, 1],
        [2, 1, 1],
        [1, 3, 1],
        [2, 3, 3],
    ],
)

k3 = s.minCost(
    3,
    [
        [2, 1, 1],
        [1, 0, 1],
        [2, 0, 16],
    ],
)

print(k1)
print(k2)
print(k3)
