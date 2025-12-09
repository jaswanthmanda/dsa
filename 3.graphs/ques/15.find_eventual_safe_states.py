# Find the eventual safe states
"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1.
The graph is represented by a 0-indexed 2D integer array graph
where graph[i] is an integer array of nodes adjacent to node i,
meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges.
A node is a safe node if every possible path starting from that node
leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""
"""
Example 1:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation:
The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.


Example 2:
Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.
"""
"""
Constraints:
- n == graph.length
- 1 <= n <= 104
- 0 <= graph[i].length <= n
- 0 <= graph[i][j] <= n - 1
- graph[i] is sorted in a strictly increasing order.
- The graph may contain self-loops.
- The number of edges in the graph will be in the range [1, 4 * 104].
"""


class Solution(object):
    def dfs(self, start, adj):
        if start in self.visited:
            return self.visited[start]

        self.pathVis.add(start)
        ans = False

        if adj[start] == []:
            self.pathVis.remove(start)
            self.visited[start] = False
            return False

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

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        self.visited = {}
        self.pathVis = set()
        n = len(graph)
        safe = []

        for i in range(n):
            # self.pathVis.clear()
            if not self.dfs(i, graph):
                safe.append(i)

        return safe


s = Solution()

k1 = s.eventualSafeNodes(
    [
        [1, 2],
        [2, 3],
        [5],
        [0],
        [5],
        [],
        [],
    ]
)

k2 = s.eventualSafeNodes(
    [
        [1, 2, 3, 4],
        [1, 2],
        [3, 4],
        [0, 4],
        [],
    ]
)

# test case skipped
# expected: [0, 1,2,3,4]
k3 = s.eventualSafeNodes(
    [
        [],
        [0, 2, 3, 4],
        [3],
        [4],
        [],
    ]
)

print(k1)
print(k2)
print(k3)
