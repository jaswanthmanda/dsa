from collections import deque

# Minimum number of vertices to reach all nodes
"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges
where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable.
It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
"""
"""
Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation:
It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5].
From 3 we can reach [3,4,2,5]. So we output [0,3].

Example 2:
Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation:
Notice that vertices 0, 3 and 2 are not reachable from
any other node, so we must include them.
Also any of these vertices can reach nodes 1 and 4.
"""
"""
Constraints:
- 2 <= n <= 10^5
- 1 <= edges.length <= min(10^5, n * (n - 1) / 2)
- edges[i].length == 2
- 0 <= fromi, toi < n
- All pairs (fromi, toi) are distinct.
"""


class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # build adj list
        adjlist = {i: [] for i in range(n)}
        kemp = set([i for i in range(n)])
        # print(kemp)

        for edge in edges:
            adjlist[edge[0]].append(edge[1])
            if edge[1] in kemp:
                kemp.remove(edge[1])

        return list(kemp)


s = Solution()

k1 = s.findSmallestSetOfVertices(
    6,
    [
        [0, 1],
        [0, 2],
        [2, 5],
        [3, 4],
        [4, 2],
    ],
)

k2 = s.findSmallestSetOfVertices(
    5,
    [
        [0, 1],
        [2, 1],
        [3, 1],
        [1, 4],
        [2, 4],
    ],
)

k3 = s.findSmallestSetOfVertices(
    3,
    [
        [1, 2],
        [1, 0],
        [0, 2],
    ],
)

print(k1)
print(k2)
print(k3)
