from collections import deque

# Shortest path with alternating colors
"""
You are given an integer n, the number of nodes in a directed
graph where the nodes are labeled from 0 to n - 1.
Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:
- redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
- blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.

Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to
node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
"""
"""
Example 1:
Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

Example 2:
Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
"""
"""
Constraints:
- 1 <= n <= 100
- 0 <= redEdges.length, blueEdges.length <= 400
- redEdges[i].length == blueEdges[j].length == 2
- 0 <= ai, bi, uj, vj < n
"""


class Solution(object):
    def shorDis(self, start, n, adjlist):
        # heapq
        dist = [[float('inf'), float('inf')] for _ in range(n)]
        dist[start][0] = dist[start][1] = 0
        q = deque()
        q.append((0, -1))

        while q:
            node, col = q.popleft()

            for nei_vals in adjlist[node]:
                nei_node, nei_col = nei_vals[0], nei_vals[1]
                if col == -1:
                    if dist[nei_node][nei_col] == float('inf'):
                        dist[nei_node][nei_col] = 1
                        q.append((nei_node, nei_col))
                elif nei_col != col:
                    if dist[nei_node][nei_col] == float('inf'):
                        dist[nei_node][nei_col] = dist[node][col] + 1
                        q.append((nei_node, nei_col))

        ans = []
        for item in dist:
            k = min(item)
            if k == float('inf'):
                ans.append(-1)
            else:
                ans.append(k)

        return ans

    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        # build adjlist
        adjlist = {i: [] for i in range(n)}
        # red -> 0
        # blue -> 1
        for edge in redEdges:
            a, b = edge[0], edge[1]
            adjlist[a].append((b, 0))

        for edge in blueEdges:
            c, d = edge[0], edge[1]
            adjlist[c].append((d, 1))

        camp = self.shorDis(0, n, adjlist)

        return camp


s = Solution()

k1 = s.shortestAlternatingPaths(3, [[0, 1], [1, 2]], [])

k2 = s.shortestAlternatingPaths(3, [[0, 1]], [[2, 1]])

# [0,1,2,3,7]
k3 = s.shortestAlternatingPaths(
    5,
    [[0, 1], [1, 2], [2, 3], [3, 4]],
    [[1, 2], [2, 3], [3, 1]],
)

print(k1)
print(k2)
print(k3)
