from collections import deque

# Minimum Height Trees
"""
A tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges
where edges[i] = [ai, bi] indicates that there is an undirected edge
between the two nodes ai and bi in the tree,
you can choose any node of the tree as the root.
When you select a node x as the root,
the result tree has height h. Among all possible rooted trees,
those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""
"""
Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation:
As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
"""
"""
Constraints:
- 1 <= n <= 2 * 104
- edges.length == n - 1
- 0 <= ai, bi < n
- ai != bi
- All the pairs (ai, bi) are distinct.
- The given input is guaranteed to be a tree and there will be no repeated edges.
"""


# Brute force (O(n**2))
class Solution(object):
    def bfs(self, start, adjList):
        q = deque()
        vis = set([start])
        q.append((start, 0))
        maxLev = 0

        while q:
            node, lev = q.popleft()
            if lev > maxLev:
                maxLev = lev

            for nei in adjList[node]:
                if nei not in vis:
                    vis.add(nei)
                    q.append((nei, lev + 1))

        return maxLev

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # build adj list
        adjList = {i: [] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        minLev = float("inf")
        ans = []

        for i in range(n):
            curr_lev = self.bfs(i, adjList)
            if minLev > curr_lev:
                minLev = curr_lev
                ans = [i]
            elif minLev == curr_lev:
                ans.append(i)

        return ans


# optimal
class SolutionOptimal:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # handle edge case
        if n == 1:
            return [0]

        # build adj list
        adjList = {i: [] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        edge_cnt = {}
        leaves = deque()
        for src, neighbours in adjList.items():
            if len(neighbours) == 1:
                leaves.append(src)
            edge_cnt[src] = len(neighbours)

        while leaves:
            if n <= 2:
                return list(leaves)

            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adjList[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)


s = SolutionOptimal()

k1 = s.findMinHeightTrees(
    4,
    [
        [1, 0],
        [1, 2],
        [1, 3],
    ],
)

k2 = s.findMinHeightTrees(
    6,
    [
        [3, 0],
        [3, 1],
        [3, 2],
        [3, 4],
        [5, 4],
    ],
)

print(k1)
print(k2)
