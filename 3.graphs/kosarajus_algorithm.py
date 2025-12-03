# Kosaraju's algorithm
"""
You are given a directed graph with V vertices, numbered from 0 to V - 1, and its adjacency list Adj,
where Adj[i] contains all vertices j such that there is a directed edge from vertex i to vertex j.


Your task is to find the number of strongly connected components (SCCs) in the graph.
"""
"""
Examples:
Input: V=5, Adj=[[2,3],[0],[1],[4],[]]
Output: 3

Input: V=8, Adj=[[1],[2],[0,3],[4],[5,7],[6],[4,7],[]]
Output: 4
"""
"""
Constraints:
- 1 ≤ V ≤ 5000
- 0 ≤ E ≤ (V*(V-1))
- 0 ≤ ai, bi ≤ V-1
"""


class Solution:
    def _dfs_corr(self, start, adj):
        self.vis[start] = True

        for node in adj[start]:
            if not self.vis[node]:
                self._dfs_corr(node, adj)

        self.stack.append(start)

    def _dfs_rev(self, start, adjT):
        self.vis[start] = True

        for node in adjT[start]:
            if not self.vis[node]:
                self._dfs_rev(node, adjT)

    def _reverse_nodes(self, V, adj):
        adjT = {i: [] for i in range(V)}

        for i in range(V):
            for node in adj[i]:
                adjT[node].append(i)

        return adjT

    def kosaraju(self, V, adj):
        """
        1. Make a dfs
        2. store them into stack
        3. reverse the nodes
        4. remove out the nodes and make a dfs through revAdj (also simultaneously check vis[])
        """
        # IMPORTANT NOTE: only it is applied for directed graphs.
        self.stack = []
        self.vis = [False for _ in range(V)]

        for i in range(V):
            if not self.vis[i]:
                self._dfs_corr(i, adj)

        adjT = self._reverse_nodes(V, adj)

        self.vis = [False for _ in range(V)]

        cnt = 0
        while self.stack:
            node = self.stack.pop()
            if not self.vis[node]:
                cnt += 1
                self._dfs_rev(node, adjT)

        return cnt


s = Solution()

k1 = s.kosaraju(
    5,
    [
        [2, 3],
        [0],
        [1],
        [4],
        [],
    ],
)

k2 = s.kosaraju(
    8,
    [
        [1],
        [2],
        [0, 3],
        [4],
        [5, 7],
        [6],
        [4, 7],
        [],
    ],
)

k3 = s.kosaraju(
    28,
    [
        [21, 15],
        [24, 14],
        [15, 16],
        [9, 25],
        [15, 11],
        [9, 17],
        [12, 8],
        [14, 27],
        [1, 15],
        [24, 13],
        [2, 19],
        [24, 26],
        [23, 8],
        [18, 15],
        [19, 3],
        [20, 6],
        [0, 4],
        [5, 24],
        [22, 20],
        [7, 13],
        [20, 10],
        [26, 9],
        [17, 12],
        [10, 12],
        [18, 3],
        [17, 25],
        [14, 21],
        [21, 3],
        [13, 19],
        [15, 9],
        [22, 10],
        [17, 8],
        [15, 8],
        [27, 8],
        [5, 7],
        [3, 17],
        [18, 4],
        [9, 16],
        [16, 21],
        [2, 24],
        [1, 25],
        [8, 14],
        [19, 9],
        [16, 4],
        [20, 19],
        [6, 13],
        [27, 3],
        [10, 26],
        [1, 3],
        [8, 15],
        [17, 25],
        [12, 9],
        [22, 27],
        [8, 1],
        [4, 15],
        [19, 16],
        [2, 17],
        [4, 27],
        [18, 12],
        [3, 14],
        [5, 19],
        [8, 4],
        [10, 26],
        [5, 13],
        [5, 12],
        [26, 13],
        [26, 8],
        [16, 9],
        [0, 21],
        [16, 9],
        [5, 15],
        [5, 14],
        [2, 27],
        [25, 23],
        [3, 15],
        [5, 18],
        [18, 17],
        [9, 24],
        [25, 6],
        [4, 21],
        [18, 21],
        [14, 13],
        [1, 7],
        [1, 17],
        [17, 5],
        [8, 13],
        [16, 6],
        [26, 12],
        [19, 7],
        [14, 8],
        [4, 8],
        [27, 14],
        [10, 12],
        [0, 26],
        [5, 22],
        [1, 19],
        [6, 20],
        [3, 26],
        [7, 13],
        [9, 19],
        [15, 4],
        [24, 9],
        [16, 13],
        [21, 27],
        [24, 1],
        [8, 19],
        [0, 19],
        [13, 16],
        [19, 8],
        [15, 16],
        [6, 5],
        [3, 23],
        [7, 1],
        [0, 14],
        [19, 15],
        [24, 5],
        [22, 14],
        [27, 18],
        [21, 13],
    ],
)

print(k1)
print(k2)
print(k3)
