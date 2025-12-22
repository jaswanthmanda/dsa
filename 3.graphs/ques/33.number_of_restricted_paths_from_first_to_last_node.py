import heapq

# Number of restricted paths from first to last node
"""
There is an undirected weighted connected graph. You are given
a positive integer n which denotes that
the graph has n nodes labeled from 1 to n, and an array edges where each
edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

There is an undirected weighted connected graph. You are given a positive integer n
which denotes that the graph has n nodes labeled from 1 to n,
and an array edges where each edges[i] = [ui, vi, weighti]
denotes that there is an edge between nodes ui and vi with weight equal to weighti.

The distance of a path is the sum of the weights
on the edges of the path. Let distanceToLastNode(x) denote
the shortest distance of a path between node n and node x.
A restricted path is a path
that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.


Return the number of restricted paths from node 1 to node n.
Since that number may be too large, return it modulo 109 + 7.
"""
"""
Example 1:
Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3
Explanation:
Each circle contains the node number in black and its distanceToLastNode value in blue. The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5

Example 2:
Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
Output: 1
Explanation:
Each circle contains the node number in black and its distanceToLastNode value in blue. The only restricted path is 1 --> 3 --> 7.
"""
"""
Constraints:
- 1 <= n <= 2 * 104
- n - 1 <= edges.length <= 4 * 104
- edges[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 1 <= weighti <= 105
- There is at most one edge between any two nodes.
- There is at least one path between any two nodes.
"""


class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        # build adjacency list
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # dijkstra from node n
        dist = [float("inf")] * (n + 1)
        dist[n] = 0
        pq = [(0, n)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue

            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))

        # DP
        memo = [-1] * (n + 1)

        def dfs(u):
            if u == n:
                return 1
            if memo[u] != -1:
                return memo[u]

            total = 0
            for v, _ in graph[u]:
                if dist[u] > dist[v]:  # restriction condition
                    total = (total + dfs(v)) % MOD

                memo[u] = total

            return total

        return dfs(1)


s = Solution()

k1 = s.countRestrictedPaths(
    5,
    [
        [1, 2, 3],
        [1, 3, 3],
        [2, 3, 1],
        [1, 4, 2],
        [5, 2, 2],
        [3, 5, 1],
        [5, 4, 10],
    ],
)

k2 = s.countRestrictedPaths(
    7,
    [
        [1, 3, 1],
        [4, 1, 2],
        [7, 3, 4],
        [2, 5, 3],
        [5, 6, 1],
        [6, 7, 2],
        [7, 5, 3],
        [2, 6, 4],
    ],
)

print(k1)
print(k2)
