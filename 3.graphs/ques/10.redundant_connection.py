# Redundant Connection
"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi]
indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.
"""
"""
Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
"""
"""
Constraints:
- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges.
- The given graph is connected.
"""


# O(n^2)
class Solution(object):
    def dfs(self, start, parent, adjList):
        self.visited.add(start)

        for nei in adjList[start]:
            if nei not in self.visited:
                ans = self.dfs(nei, start, adjList)
                if ans:
                    return True
            elif nei != parent:
                return True

        return False

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # build adj list
        adjList = {}

        def add_edge(u, v):
            if u not in adjList:
                adjList[u] = []
            if v not in adjList:
                adjList[v] = []

            adjList[u].append(v)
            adjList[v].append(u)

        for items in edges:
            u, v = items[0], items[1]
            add_edge(u, v)

            if u in adjList and v in adjList:
                self.visited = set()
                # print(u, v, self.dfs(u, -1, adjList))
                if self.dfs(u, -1, adjList):
                    return [u, v]


class DisjointSet:
    def __init__(self, maxNode):
        self.nodes = [i for i in range(1, maxNode + 1)]
        self.parent = [i for i in range(1, maxNode + 1)]
        self.sizes = [1 for _ in range(1, maxNode + 1)]

    def findUParent(self, u):
        if u == self.parent[u - 1]:
            return u

        self.parent[u - 1] = self.findUParent(self.parent[u - 1])

        return self.parent[u - 1]

    def unionBySizes(self, u, v):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)

        if ulp_u == ulp_v:
            return None

        if self.sizes[ulp_u - 1] < self.sizes[ulp_v - 1]:
            self.parent[ulp_u - 1] = ulp_v
            self.sizes[ulp_v - 1] += self.sizes[ulp_u - 1]
        else:
            self.parent[ulp_v - 1] = ulp_u
            self.sizes[ulp_u - 1] += self.sizes[ulp_v - 1]


# optimal O(n)
class SolutionOptimal:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        maxNode = 0
        for u, v in edges:
            maxNode = max(maxNode, u, v)

        ds = DisjointSet(maxNode)

        for u, v in edges:
            if ds.findUParent(u) == ds.findUParent(v):
                return [u, v]
            else:
                ds.unionBySizes(u, v)


s = SolutionOptimal()

k1 = s.findRedundantConnection(
    [
        [1, 2],
        [1, 3],
        [2, 3],
    ]
)

k2 = s.findRedundantConnection(
    [
        [1, 2],
        [2, 3],
        [3, 4],
        [1, 4],
        [1, 5],
    ]
)

print(k1)
print(k2)
