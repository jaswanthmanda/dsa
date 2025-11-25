from collections import deque

# Shortest path in undirected graph with unit weights
"""
Given a Undirected Graph of N vertices from 0 to N-1 and M edges and a 2D Integer array edges,
where there is a edge from vertex edges[i][0] to vertex edges[i][1] of unit weight.

Find the shortest path from the source to all other nodes in this graph.
In this problem statement, we have assumed the source vertex to be '0'.
If a vertex is unreachable from the source node, then return -1 for that vertex.
"""
"""
Input: n = 9, m = 10, edges = [[0,1],[0,3],[3,4],[4,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]
Output: 0 1 2 1 2 3 3 4 4
Explanation:
The above output array shows the shortest path to all
the nodes from the source vertex (0), Dist[0] = 0, Dist[1] = 1 , Dist[2] = 2 , …. Dist[8] = 4.
Where Dist[node] is the shortest path between src and the node. For a node,
if the value of Dist[node]= -1,
then we conclude that the node is unreachable from the src node.


Input: n = 8, m = 10, edges =[[1,0],[2,1],[0,3],[3,7],[3,4],[7,4],[7,6],[4,5],[4,6],[6,5]]
Output: 0 1 2 1 2 3 3 2
Explanation:
The above output list shows the shortest path to all the nodes from the source vertex (0),
Dist[0] = 0, Dist[1] = 1, Dist[2] = 2,.....Dist[7] = 2.
"""
"""
Constraints:
- 1<=n,m<=104
- 0<=edges[i][j]<=n-1
"""


class Solution:
    def bfs(self, start, adj):
        q = deque([(start, 0)])
        visited = set()
        visited.add(start)

        while q:
            node, wt = q.popleft()
            self.ans[node] = wt

            for nei in adj[node]:
                if nei[0] not in visited:
                    visited.add(nei[0])
                    q.append((nei[0], wt + nei[1]))

    def shortestPath(self, edges, N, M):
        # build adj matrix
        adj = {i: [] for i in range(N)}

        for i in edges:
            a, b = i[0], i[1]
            adj[a].append((b, 1))
            adj[b].append((a, 1))

        # print(adj)

        self.ans = [-1 for _ in range(N)]
        self.ans[0] = 0

        self.bfs(0, adj)

        return self.ans


s = Solution()

k1 = s.shortestPath(
    [
        [0, 1],
        [0, 3],
        [3, 4],
        [4, 5],
        [5, 6],
        [1, 2],
        [2, 6],
        [6, 7],
        [7, 8],
        [6, 8],
    ],
    9,
    10,
)

k2 = s.shortestPath(
    [
        [1, 0],
        [2, 1],
        [0, 3],
        [3, 7],
        [3, 4],
        [7, 4],
        [7, 6],
        [4, 5],
        [4, 6],
        [6, 5],
    ],
    8,
    10,
)

print(k1)
print(k2)
