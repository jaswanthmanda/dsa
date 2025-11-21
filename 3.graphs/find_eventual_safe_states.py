# Find eventual safe states
"""
Given a directed graph with V vertices labeled from 0 to V-1.
The graph is represented using an adjacency list where adj[i] lists
all nodes adjacent to node i, meaning there is an edge from node i to each node in adj[i].
A node is a terminal node if there are no outgoing edges.
A node is a safe node if every possible path starting from that node leads to a terminal node.
Return an array containing all the safe nodes of the graph in ascending order.
"""
"""
Input: V = 7, adj= [[1,2], [2,3], [5], [0], [5], [], []]
Output: [2, 4, 5, 6]
Explanation: 
From node 0: two paths are there 0->2->5 and 0->1->3->0. 
The second path does not end at a terminal node. So it is not a safe node.
From node 1: two paths exist: 1->3->0->1 and 1->2->5.
But the first one does not end at a terminal node. So it is not a safe node.
But the first one does not end at a terminal node. So it is not a safe node.
So it is a safe node.
From node 3: two paths: 3->0->1->3 and 3->0->2->5 
but the first path does not end at a terminal node. 
So it is not a safe node.
From node 4: Only one path: 4->5 and 5 is a terminal node. 
So it is also a safe node.
From node 5: It is a terminal node. 
So it is a safe node as well.
From node 6: It is a terminal node. 
So it is a safe node as well.


Input: V = 4, adj= [[1], [2], [0,3], []]
Output: [3]
Explanation:
Node 3 itself is a terminal node and it is a safe node as well.
But all the paths from other nodes do not lead to a terminal node.So they are excluded from the answer.
"""

"""
Constraints:
- V == adj.length
- 1 <= V <= 104
- 0 <= adj[i].length <= n
- 0 <= adj[i][j] <= n - 1
- adj[i] is sorted in a strictly increasing order.
- The graph may contain self-loops.
- The number of edges in the graph will be in the range [1, 4 * 104].
"""


class Solution:
    def validate(self, V, adj):
        # 1. Check adjacency list length
        if len(adj) != V:
            return False

        for i in range(V):
            prev = -1
            for v in adj[i]:
                # 2. Out-of-range value
                if v < 0 or v >= V:
                    return False
                # 3. Must be strictly increasing (given by constraints)
                if v <= prev:
                    return False
                prev = v

        return True

    def dfs(self, start, adj):
        if start in self.visited:
            return self.visited[start]

        self.pathVis.add(start)

        if adj[start] == []:
            self.visited[start] = False
            return False

        ans = False
        for nei in adj[start]:
            if nei in self.pathVis:
                ans = True
                break
            if self.dfs(nei, adj):
                ans = True
                break

        self.pathVis.remove(start)
        self.visited[start] = ans
        return ans

    def eventualSafeNodes(self, V, adj):
        # Validate input BEFORE processing
        if not self.validate(V, adj):
            return "Invalid Input"

        self.visited = {}
        self.pathVis = set()
        safe = []

        for i in range(V):
            self.pathVis.clear()
            if not self.dfs(i, adj):
                safe.append(i)

        return safe


s = Solution()

k1 = s.eventualSafeNodes(
    7,
    [
        [1, 2],
        [2, 3],
        [5],
        [0],
        [5],
        [],
        [],
    ],
)

k2 = s.eventualSafeNodes(
    4,
    [
        [1],
        [2],
        [0, 3],
        [],
    ],
)

k3 = s.eventualSafeNodes(
    23,
    [
        [],
        [8],
        [15, 6],
        [0, 13],
        [16, 1, 0],
        [12, 19],
        [3],
        [],
        [],
        [],
        [15],
        [15],
        [22],
        [],
        [],
        [],
        [4, 16],
        [1],
        [6, 20],
        [7, 4, 12, 8, 11, 2],
        [14, 20, 18],
        [],
        [14, 5, 6, 3],
    ],
)

print(k1)
print(k2)
print(k3)
