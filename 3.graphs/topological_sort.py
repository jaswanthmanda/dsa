# Topological sort or Kahn's algorithm
"""
Given a Directed Acyclic Graph (DAG) with V vertices labeled from 0 to V-1.
The graph is represented using an adjacency list where adj[i] lists all nodes connected to node.
Find any Topological Sorting of that Graph.

In topological sorting, node u will always appear before node v if there is a directed edge from node u towards node v(u -> v).

The function should return an array representing the topological order.
The output will be validated by our driver code, which checks the correctness of your topological sort.
It will print True if the order is valid, otherwise False.
"""
"""
Input: V = 6,adj=[ [ ], [ ], [3], [1], [0,1], [0,2] ]
Output: [5, 4, 2, 3, 1, 0]
Explanation:
A graph may have multiple topological sortings.
- Node 5 must appear before 0 and 2
- Node 2 must appear before 3
- Node 3 must appear before 1
- Node 4 must appear before 0 and 1

One valid topological order is: [5, 4, 2, 3, 1, 0]
"""
"""
Input: V = 4, adj=[ [ ], [0], [0], [0] ]
Output: [3, 2, 1, 0]
Explanation:
The necessary conditions for the ordering are:
- Nodes 1, 2, and 3 must all appear before 0.
- Their internal order doesn’t matter.

One valid topological order is: [3, 2, 1, 0]
"""
"""
Constraints:
- 1 ≤ V ≤ 10⁴
- 0 ≤ number of edges ≤ 10⁴
"""


class Solution:
    def dfs(self, start, adj):
        self.visited.add(start)

        for nei in adj[start]:
            if nei not in self.visited:
                self.dfs(nei, adj)

        self.stack.append(start)

    def topoSort(self, V, adj):
        self.stack = []
        self.visited = set()

        for i in range(V):
            if i not in self.visited:
                self.dfs(i, adj)

        ans = []
        while self.stack:
            ans.append(self.stack.pop())

        return ans


s = Solution()

k1 = s.topoSort(
    6,
    [
        [],
        [],
        [3],
        [1],
        [0, 1],
        [0, 2],
    ],
)

k2 = s.topoSort(
    4,
    [
        [],
        [0],
        [0],
        [0],
    ],
)

print(k1)
print(k2)
