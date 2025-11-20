from collections import deque

# Detect a cycle in an undirected graph
"""
Given an undirected graph with V vertices labeled from 0 to V-1.
The graph is represented using an adjacency list where adj[i] lists all nodes connected to node.
Determine if the graph contains any cycles.
Note: The graph does not contain any self-edges (edges where a vertex is connected to itself).
"""

"""
Input: V = 6, adj= [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
Output: True
Explanation: The graph contains a cycle: 0 ->1 -> 2 -> 5 -> 4 -> 1.


Input: V = 4, adj= [[1, 2], [0], [0, 3], [2]]
Output: False
Explanation: The graph does not contain any cycles.
"""


class Solution:
    def bfs(self, start, adj):
        q = deque([(start, -1)])
        self.visited.add(start)

        while q:
            node, parent = q.popleft()

            for adjNode in adj[node]:
                if adjNode not in self.visited:
                    self.visited.add(adjNode)
                    q.append(((adjNode, node)))
                elif parent != adjNode:
                    return True

        return False

    def isCycle(self, V, adj):
        self.visited = set([])
        for i in range(V):
            if i not in self.visited:
                if self.bfs(i, adj):
                    return True

        return False

    # def isCycle(self, V, adj):


s = Solution()

k1 = s.isCycle(
    6,
    [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [1, 3, 5],
        [2, 4],
    ],
)

k2 = s.isCycle(
    4,
    [
        [1, 2],
        [0],
        [0, 3],
        [2],
    ],
)

k3 = s.isCycle(
    24,
    [
        [],
        [],
        [20, 18, 10, 23],
        [14],
        [10],
        [],
        [22, 7, 20, 11],
        [12, 6, 22],
        [16, 15, 12, 13],
        [20],
        [17, 4, 2],
        [6],
        [7, 8],
        [23, 8],
        [22, 3],
        [22, 8],
        [8],
        [10],
        [2],
        [23],
        [2, 21, 6, 9],
        [20],
        [6, 14, 15, 7],
        [13, 19, 2],
    ],
)

print(k1)
print(k2)
print(k3)
