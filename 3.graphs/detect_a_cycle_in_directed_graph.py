# Detect a cycle in a directed graph
"""
Given a directed graph with V vertices labeled from 0 to V-1.
The graph is represented using an adjacency list where adj[i] lists all nodes connected to node.
Determine if the graph contains any cycles.
"""
"""
Input: V = 6, adj= [ [1], [2, 5], [3], [4], [1], [ ] ]
Output: True
Explanation: The graph contains a cycle: 1 -> 2 -> 3 -> 4 -> 1.
"""
"""
Input: V = 4, adj= [[1,2], [2], [], [0,2]]
Output: False
Explanation:
The graph does not contain a cycle.
"""
"""
Constraints:
- E=number of edges
- 1 ≤ V, E ≤ 104
"""


class Solution:
    def dfs(self, start, adj):
        self.visited.add(start)
        self.pathVisited.add(start)

        for nei in adj[start]:
            if nei not in self.visited:
                if self.dfs(nei, adj):
                    return True
            elif nei in self.visited and nei in self.pathVisited:
                return True

        self.pathVisited.remove(start)
        return False

    def isCyclic(self, N, adj):
        self.visited = set()
        self.pathVisited = set()

        for i in range(N):
            if i not in self.visited:
                if self.dfs(i, adj):
                    return True

        return False


s = Solution()

k1 = s.isCyclic(
    6,
    [
        [1],
        [2, 5],
        [3],
        [4],
        [1],
        [],
    ],
)

k2 = s.isCyclic(
    4,
    [
        [1, 2],
        [2],
        [],
        [0, 2],
    ],
)

print(k1)
print(k2)
