from collections import deque

# Shortest path in DAG
"""
Given a Directed Acyclic Graph of N vertices from 0 to N-1
and M edges and a 2D Integer array edges,
where there is a directed edge from vertex edge[i][0] to vertex
edge[i][1] with a distance of edge[i][2] for all i.

Find the shortest path from source vertex to all the vertices and
if it is impossible to reach any vertex, then return -1 for that vertex.
The source vertex is assumed to be 0.
"""
"""
Input: N = 4, M = 2 edge = [[0,1,2],[0,2,1]]
Output: 0 2 1 -1
Explanation:
Shortest path from 0 to 1 is 0->1 with edge weight 2.
Shortest path from 0 to 2 is 0->2 with edge weight 1.
Shortest path from 0 to 2 is 0->2 with edge weight 1.


Input: N = 6, M = 7 edge = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
Output: 0 2 3 6 1 5
Explanation:
Shortest path from 0 to 1 is 0->1 with edge weight 2.
Shortest path from 0 to 2 is 0->4->2 with edge weight 1+2=3.
Shortest path from 0 to 3 is 0->4->5->3 with edge weight 1+4+1=6.
Shortest path from 0 to 4 is 0->4 with edge weight 1.
Shortest path from 0 to 5 is 0->4->5 with edge weight 1+4=5.
"""
"""
Constraints:
- 1 ≤ N,M ≤ 5*104
- 0 ≤ edge[i][0],edge[i][1] < N-1
- 1 ≤ edge[i][2] < 104
"""


class Solution:

    # my approach
    def shortestPath(self, N, M, edges):
        # build adj
        adj = {i: [] for i in range(N)}
        for i in range(len(edges)):
            a, b, c = edges[i][0], edges[i][1], edges[i][2]
            adj[a].append((b, c))

        ans = [float("inf") for _ in range(N)]
        ans[0] = 0
        q = deque([0])

        while q:
            node = q.popleft()

            for nei, wt in adj[node]:
                if ans[node] + wt < ans[nei]:
                    ans[nei] = ans[node] + wt
                    q.append((nei))

        # convert unreachable nodes
        for i in range(N):
            if ans[i] == float("inf"):
                ans[i] = -1

        return ans

    def shortestPathTopo(self, N, M, edges):
        # build adj
        adj = {i: [] for i in range(N)}
        indegree = [0] * N
        for i in range(len(edges)):
            a, b, c = edges[i][0], edges[i][1], edges[i][2]
            adj[a].append((b, c))
            indegree[b] += 1

        # Step 1: Topological Sort (Kahn's Algorithm)
        q = deque()
        for i in range(N):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            for nei, wt in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        # Step 2: Shortest Path initialization
        dist = [float("inf")] * N
        dist[0] = 0

        # Step 3: Relax edges in topo order
        for node in topo:
            if dist[node] != float("inf"):  # skip unreachable
                for nei, wt in adj[node]:
                    if dist[node] + wt < dist[nei]:
                        dist[nei] = dist[node] + wt

        # Step 4: Convert unreachable nodes
        for i in range(N):
            if dist[i] == float("inf"):
                dist[i] = -1

        return dist


s = Solution()

k1 = s.shortestPath(
    4,
    2,
    [
        [0, 1, 2],
        [0, 2, 1],
    ],
)

k2 = s.shortestPath(
    6,
    7,
    [
        [0, 1, 2],
        [0, 4, 1],
        [4, 5, 4],
        [4, 2, 2],
        [1, 2, 3],
        [2, 3, 6],
        [5, 3, 1],
    ],
)

k3 = s.shortestPathTopo(
    4,
    2,
    [
        [0, 1, 2],
        [0, 2, 1],
    ],
)

k4 = s.shortestPathTopo(
    6,
    7,
    [
        [0, 1, 2],
        [0, 4, 1],
        [4, 5, 4],
        [4, 2, 2],
        [1, 2, 3],
        [2, 3, 6],
        [5, 3, 1],
    ],
)

print(k1)
print(k2)
print(k3)
print(k4)
