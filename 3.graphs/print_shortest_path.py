import heapq

# Print Shortest Path
"""
Given a weighted undirected graph having n vertices numbered from 1 to n and m edges describing there are edges,
where edges[i]=[ai,bi,wi],
representing an edge from vertex ai to bi with weight wi.

Find the shortest path between the vertex 1 and the vertex n
and if path does not exist then return a list consisting of only -1.

If there exists a path, then return a list whose first element
is the weight of the path and the remaining elements represent
the shortest path from vertex 1 to vertex n.

Note: On IDE only the total sum of weights will be shown as output.
As there might be more than one path (The path will be validated through driver code and
If wrong then output shown will be -2.).
"""
"""
Input: n = 5, m= 6, edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
Output: 5 1 4 3 5
Explanation:
Explanation:
The source vertex is 1.
Hence, the shortest distance path of node 5 from the source will be 1->4->3->5 as this is the path with a minimum sum
of edge weights from source to destination.

Input: n = 4, m = 4, edges = [[1,2,2], [2,3,4], [1,4,1],[4,3,3]]
Output:1 1 4
Explanation:
The source vertex is 1. Hence, the shortest distance path of node 4 from
the source will be 1->4 as this is the path with
the minimum sum of edge weights from source to destination.
"""
"""
Constraints:
- 2 <= n <= 104
- 0 <= m <= 2*104
- 1 <= a, b <= n
- 1 <= w <= 105
"""


class Solution:
    def shortestPath(self, n, m, edges):
        # build adj matrix
        adj = {i: [] for i in range(1, n + 1)}

        for ai, bi, wi in edges:
            adj[ai].append((bi, wi))
            adj[bi].append((ai, wi))

        ans = [float('inf') for _ in range(n + 1)]

        pq = [(0, 1)]
        ans[1] = 0
        parent = [-1] * (n + 1)
        while pq:
            wt, node = heapq.heappop(pq)

            if wt > ans[node]:
                continue

            for nei, nei_wt in adj[node]:
                if wt + nei_wt < ans[nei]:
                    ans[nei] = wt + nei_wt
                    parent[nei] = node
                    heapq.heappush(pq, (wt + nei_wt, nei))

        if parent[n] == -1:
            return [-1]

        path = []
        curr = n
        while curr != -1:
            path.append(curr)
            curr = parent[curr]

        path.reverse()

        return [ans[n]] + path


s = Solution()

k1 = s.shortestPath(
    5,
    6,
    [
        [1, 2, 2],
        [2, 5, 5],
        [2, 3, 4],
        [1, 4, 1],
        [4, 3, 3],
        [3, 5, 1],
    ],
)

k2 = s.shortestPath(
    4,
    4,
    [
        [1, 2, 2],
        [2, 3, 4],
        [1, 4, 1],
        [4, 3, 3],
    ],
)

print(k1)
print(k2)
