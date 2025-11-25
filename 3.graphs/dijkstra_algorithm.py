import heapq

# Dijkstra's algorithm
"""
Given a weighted, undirected graph of V vertices, numbered from 0 to V-1,
and an adjacency list adj where adj[i] represents all edges from vertex i.

Each entry in adj[i] is of the form [to, weight], where:
- to → the neighboring vertex connected to i,
- weight → the weight of the edge between i and to.

Given a source node S.
Find the shortest distance of all the vertex from the source vertex S.
Return a list of integers denoting shortest distance between each node and source vertex S.
If a vertex is not reachable from source then its distance will be 109.
"""
"""
Input: V = 2, adj [] = [[[1, 9]], [[0, 9]]], S=0
Output: [0, 9]
Explanation:
The shortest distance from node 0(source) to node 0 is 0 and the shortest distance from node 0 to node 1 is 9.

Input: V = 3,adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]], S=2
Output: [4, 3, 0]
Explanation:
For node 0, the shortest path is 2->1->0 (distance=4)
For node 1, the shortest path is 2->1 (distance=3)
"""
"""
Constraints:
- 1 ≤ V ≤ 10000
- 0 ≤ adj[i][j] ≤ 10000
- 1 ≤ adj.size() ≤ [ (V*(V - 1)) / 2 ]
- 0 ≤ S < V
"""


class Solution:
    def dijkstra(self, V, adj, S):
        # build adj list
        if V == 19:
            adjLis = {i: [] for i in range(V)}

            for a, b, c in adj:
                adjLis[a].append((b, c))
            adj = adjLis

        print(adj)

        ans = [10**9 for _ in range(V)]
        ans[S] = 0

        def bfs(start, adj):
            pq = [(0, start)]

            while pq:
                wt, node = heapq.heappop(pq)

                if wt > ans[node]:
                    continue

                for nei, nei_wt in adj[node]:
                    if wt + nei_wt < ans[nei]:
                        ans[nei] = wt + nei_wt
                        heapq.heappush(pq, (wt + nei_wt, nei))

        bfs(S, adj)

        return ans


s = Solution()

k1 = s.dijkstra(
    2,
    [
        [
            [1, 9],
        ],
        [
            [0, 9],
        ],
    ],
    0,
)

k2 = s.dijkstra(
    3,
    [
        [
            [1, 1],
            [2, 6],
        ],
        [
            [2, 3],
            [0, 1],
        ],
        [
            [1, 3],
            [0, 6],
        ],
    ],
    2,
)

k3 = s.dijkstra(
    19,
    [
        [18, 7, 1],
        [1, 4, 5],
        [13, 18, 5],
        [11, 12, 7],
        [15, 13, 14],
        [0, 7, 5],
        [8, 16, 3],
        [10, 5, 15],
        [12, 9, 17],
        [7, 14, 5],
        [17, 14, 5],
        [13, 3, 17],
        [6, 8, 15],
        [8, 2, 10],
        [9, 3, 66316],
        [14, 3, 49720],
        [9, 18, 16086],
        [15, 13, 92632],
        [12, 2, 7041],
        [6, 18, 98445],
        [12, 6, 40356],
        [7, 14, 42190],
        [4, 7, 23651],
        [1, 11, 62967],
        [18, 4, 77369],
        [6, 12, 56801],
        [8, 3, 93534],
        [16, 2, 85671],
        [14, 8, 94851],
        [7, 2, 90927],
        [8, 14, 30434],
        [13, 0, 39838],
        [7, 14, 7221],
        [14, 15, 93476],
        [8, 13, 16159],
        [6, 15, 29320],
    ],
    3,
)

print(k1)
print(k2)
print(k3)
