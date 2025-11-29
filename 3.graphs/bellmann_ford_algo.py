# Bellman ford algorithm
"""
Given a weighted and directed graph of V vertices and E edges. An edge is represented as [ai, bi, wi],
meaning there is a directed edge from ai to bi having weight wi.
Find the shortest distance of all the vertices from the source vertex S.
If a vertex can't be reached from the S then mark the distance as 109.

If the graph contains a negative cycle then return -1 in a list.
"""
"""
Input : V = 6, Edges = [[3, 2, 6], [5, 3, 1], [0, 1, 5], [1, 5, -3], [1, 2, -2], [3, 4, -2], [2, 4, 3]], S = 0
Output: 0 5 3 3 1 2
Explanation:
- For node 1, shortest path is 0->1 (distance=5).
- For node 2, shortest path is 0->1->2 (distance=3)
- For node 3, shortest path is 0->1->5->3 (distance=3)
- For node 4, shortest path is 0->1->5->3->4 (distance=1)
- For node 5, shortest path is 0->1->5 (distance=2)

Input : V = 2, Edges = [[0,1,9]], S = 0
Output: 0 9
Explanation:
For node 1, the shortest path is 0->1 (distance=9)
"""
"""
Constraints:
- 1 ≤ V ≤ 500
- 1 ≤ E ≤ V*(V-1)
- -1000 ≤ edges[i][3] ≤ 1000
- 0 ≤ S < V
"""
"""
Custom Testcase:
V = 16
edges = [[9,14,19],[5,1,77],[2,15,22],[2,11,18],[7,2,37],[7,0,41],[14,10,95],[8,7,-16],[1,10,52],[12,6,35],[4,5,11],[7,3,2],[12,9,75],[13,4,84],[8,12,48],[0,5,91],[6,11,86],[1,13,69],[12,1,36]]
s = 6


V = 3
Edges = [[0,1,1000000000],[1,2,1000000000],[0,2,2000000000]]
S = 0
"""


class Solution:
    def bellman_ford(self, V, edges, S):
        # bellman ford algo imp.
        n = len(edges)
        dist = [float("inf") for _ in range(V)]
        dist[S] = 0

        for i in range(V - 1):
            for j in range(n):
                u, v, w = edges[j][0], edges[j][1], edges[j][2]
                if -1000 <= w <= 1000 and dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for jj in range(n):
            u, v, w = edges[jj][0], edges[jj][1], edges[jj][2]
            if -1000 <= w <= 1000 and dist[u] != float("inf") and dist[u] + w < dist[v]:
                return [-1]

        for ii in range(V):
            if dist[ii] == float("inf"):
                dist[ii] = 10**9

        return dist


s = Solution()

k1 = s.bellman_ford(
    6,
    [
        [3, 2, 6],
        [5, 3, 1],
        [0, 1, 5],
        [1, 5, -3],
        [1, 2, -2],
        [3, 4, -2],
        [2, 4, 3],
    ],
    0,
)

k2 = s.bellman_ford(
    2,
    [
        [0, 1, 9],
    ],
    0,
)

k3 = s.bellman_ford(
    16,
    [
        [9, 14, 19],
        [5, 1, 77],
        [2, 15, 22],
        [2, 11, 18],
        [7, 2, 37],
        [7, 0, 41],
        [14, 10, 95],
        [8, 7, -16],
        [1, 10, 52],
        [12, 6, 35],
        [4, 5, 11],
        [7, 3, 2],
        [12, 9, 75],
        [13, 4, 84],
        [8, 12, 48],
        [0, 5, 91],
        [6, 11, 86],
        [1, 13, 69],
        [12, 1, 36],
    ],
    6,
)

k4 = s.bellman_ford(
    3,
    [
        [0, 1, 1000000000],
        [1, 2, 1000000000],
        [0, 2, 2000000000],
    ],
    0,
)

k4 = s.bellman_ford(
    3,
    [
        [0, 1, 1000000000],
        [1, 2, 1000000000],
        [0, 2, 2000000000],
    ],
    0,
)

print(k1)
print(k2)
print(k3)
print(k4)
