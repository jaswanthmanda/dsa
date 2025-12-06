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


class Solution(object):
    def dfs(self, start, parent, adjList):
        self.visiting.add(start)

        ans = None

        for nei in adjList[start]:
            print(parent, start, nei)
            if nei not in self.visited and nei not in self.visiting:
                ans = self.dfs(nei, start, adjList)
            elif nei in self.visiting:
                return (start, nei)

        self.visiting.remove(start)
        self.visited.add(start)

        return ans

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # build adj list
        maxNode = 0

        for item in edges:
            maxNode = max(maxNode, item[0])
            maxNode = max(maxNode, item[1])

        adjList = {i: [] for i in range(1, maxNode + 1)}

        for item in edges:
            adjList[item[0]].append(item[1])
            adjList[item[1]].append(item[0])

        print(adjList)

        self.visited = set()
        self.visiting = set()

        ans = self.dfs(1, -1, adjList)

        return [ans[0], ans[1]]


s = Solution()

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
