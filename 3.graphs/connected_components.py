from collections import deque

# Connected Components
"""
Given a undirected Graph consisting of V vertices numbered from 0 to V-1 and E edges.
The ith edge is represented by [ai,bi], denoting a edge between vertex ai and bi.
We say two vertices u and v belong to a same component
if there is a path from u to v or v to u.
Find the number of connected components in the graph.


A connected component is a subgraph of a graph in which there exists a path between any two vertices,
and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.
"""

"""
Input: V=4, edges=[[0,1],[1,2]]
Output: 2
Explanation: Vertices {0,1,2} forms the first component
    and vertex 3 forms the second component
"""

"""
Input: V = 7, edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
Output: 3
Explanation:
The edges [0, 1], [1, 2], [2, 3] form a connected component with vertices {0, 1, 2, 3}.
The edge [4, 5] forms another connected component with vertices {4, 5}.
Therefore, the graph has 3 connected components: {0, 1, 2, 3}, {4, 5}, and the isolated vertices {6} (vertices 6 and any other unconnected vertices).
"""

"""
Example:
Input: V = 16, edges = [[3,2],[10,14],[15,0],[5,9],[3,0],[13,12],[0,5],[8,3],[13,15],[9,4],[10,11],[4,12],[5,15],[9,5]]
Output: 2
"""

"""
Constraints:
1 ≤ V, edges.length ≤ 104
0 <= edges[i][0], edges[i][1] <= V-1
All edges are unique
"""


class Solution:
    def __init__(self):
        self.visited = set()

    def bfs(self, startPoint, graph):
        if startPoint in self.visited:
            return 0

        order = []
        q = deque([startPoint])
        self.visited.add(startPoint)
        while q:
            node = q.popleft()
            order.append(node)
            for nei in graph[node]:
                if nei not in self.visited:
                    self.visited.add(nei)
                    q.append(nei)

        return 1

    def findNumberOfComponent(self, V, edges):
        self.visited = set()
        ans = 0

        adjLis = [[] for _ in range(V)]
        for u, v in edges:
            adjLis[u].append(v)
            adjLis[v].append(u)

        for i in range(V):
            ans += self.bfs(i, adjLis)

        return ans


s = Solution()
k1 = s.findNumberOfComponent(7, [[0, 1], [1, 2], [2, 3], [4, 5]])
k2 = s.findNumberOfComponent(4, [[0, 1], [1, 2]])
print(k1)
print(k2)
