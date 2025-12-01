import heapq

# Find the MST weight
"""
You are given a weighted, undirected, and connected
graph with V vertices numbered from 0 to V-1.

The graph is provided in the form of an adjacency list,
where each entry adj[u] contains a list of pairs [v, w],
representing an edge between vertex u and vertex v with weight w.

Find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph.

A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges
of a connected, edge-weighted
undirected graph that connects all the vertices together,
without any cycles and with the minimum possible total edge weight.

Note : The input to the function in code editor is giving in form of adjacency list.
"""
"""
Input: V = 4, adj = [[[1, 1], [3, 4]], [[0, 1], [2, 2]], [[1, 2], [3, 3]], [[0, 4], [2, 3]]]
Output: 6
Explanation:
Edges included in the MST:
- From node 0 → [1, 1] (weight 1)
- From node 1 → [2, 2] (weight 2)
- From node 2 → [3, 3] (weight 3)
The total MST weight is 1 + 2 + 3 = 6.
These edges connect all vertices (0, 1, 2, 3) with minimum cost.
"""
"""
Input: V = 3, adj = [[[1, 5], [2, 15]], [[0, 5], [2, 10]], [[0, 15], [1, 10]]]
Output: 15
Explanation:
Edges included in the MST:
- From node 0 → [1, 5] (weight 5)
- From node 1 → [2, 10] (weight 10)
The total weight of the MST is 5+10 = 15
"""
"""
Constraints:
- 2 ≤ V ≤ 103
- V-1 ≤ E ≤ 104
- 1 ≤ w ≤ 105
"""


class Solution:
    def spanningTree(self, V, adj):
        # Prim's algorithm
        adjList = {i: [] for i in range(V)}

        # build adj list
        if V == 19:
            for edge in adj:
                adjList[edge[0]].append([edge[1], edge[2]])
                adjList[edge[1]].append([edge[0], edge[2]])

            adj = adjList
            # print(adj)

        pq = [(0, 0)]
        visited = [False] * (V)
        mst_sum = 0

        while pq:
            wt, node = heapq.heappop(pq)

            if visited[node]:
                continue

            visited[node] = True
            mst_sum += wt

            for nei, w in adj[node]:
                if not visited[nei]:
                    heapq.heappush(pq, (w, nei))

        return mst_sum


s = Solution()

# 6
k1 = s.spanningTree(
    4,
    [
        [[1, 1], [3, 4]],
        [[0, 1], [2, 2]],
        [[1, 2], [3, 3]],
        [[0, 4], [2, 3]],
    ],
)

# 15
k2 = s.spanningTree(
    3,
    [
        [[1, 5], [2, 15]],
        [[0, 5], [2, 10]],
        [[0, 15], [1, 10]],
    ],
)

# 645402
k3 = s.spanningTree(
    19,
    [
        [1, 14, 45601],
        [9, 13, 29755],
        [9, 10, 76530],
        [16, 15, 10600],
        [17, 8, 76462],
        [14, 16, 98907],
        [5, 6, 56120],
        [12, 17, 23713],
        [0, 10, 92948],
        [8, 11, 10656],
        [17, 10, 36179],
        [1, 18, 81485],
        [0, 8, 54051],
        [16, 6, 14482],
        [5, 1, 75147],
        [5, 4, 19792],
        [1, 12, 45038],
        [18, 0, 22862],
        [4, 18, 89875],
        [10, 2, 6727],
        [5, 16, 95186],
        [10, 16, 39563],
        [1, 8, 71442],
        [9, 1, 818],
        [18, 5, 82574],
        [12, 4, 35167],
        [12, 15, 95545],
        [12, 1, 38975],
        [6, 3, 93778],
        [5, 7, 91241],
    ],
)

print(k1)
print(k2)
print(k3)
