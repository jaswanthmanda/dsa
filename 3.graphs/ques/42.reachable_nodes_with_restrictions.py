from collections import deque

# Reachable nodes with restrictions
"""
There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there
is an edge between nodes ai and bi in the tree.
You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.
"""
"""
Example 1:
Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
Output: 4
Explanation:
The diagram above shows the tree.
We have that [0,1,2,3] are the only nodes that can be reached from node 0 without visiting a restricted node.

Example 2:
Input: n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
Output: 3
Explanation:
The diagram above shows the tree.
We have that [0,5,6] are the only nodes that can be reached from node 0 without visiting a restricted node.
"""
"""
Constraints:
- 2 <= n <= 105
- edges.length == n - 1
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- edges represents a valid tree.
- 1 <= restricted.length < n
- 1 <= restricted[i] < n
- All the values of restricted are unique.
"""


class DisjointSet:
    def __init__(self, V):
        self.nodes = [i for i in range(V)]
        self.parents = [i for i in range(V)]
        self.sizes = [1 for i in range(V)]

    def findUPar(self, u):
        if self.parents[u] == u:
            return u

        self.parents[u] = self.findUPar(self.parents[u])

        return self.parents[u]

    def unionBySizes(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        if self.sizes[ulp_u] < self.sizes[ulp_v]:
            self.parents[ulp_u] = ulp_v
            self.sizes[ulp_v] += self.sizes[ulp_u]
        else:
            self.parents[ulp_v] = ulp_u
            self.sizes[ulp_u] += self.sizes[ulp_v]


class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        ds = DisjointSet(n)

        rest_set = set(restricted)
        for u, v in edges:
            if u not in rest_set and v not in rest_set:
                ds.unionBySizes(u, v)

        cnt = 0
        for i in range(n):
            if i not in rest_set and ds.findUPar(i) == ds.findUPar(0):
                print(i)
                cnt += 1

        return cnt


class Solution2(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        # build adjlist
        adjlist = {i: [] for i in range(n)}
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        kemp = set(restricted)

        def bfs(start, node):
            vis = set([start])
            q = deque([start])
            cnt = 1

            while q:
                node = q.popleft()

                for nei in adjlist[node]:
                    if nei not in kemp and nei not in vis:
                        vis.add(nei)
                        q.append(nei)
                        cnt += 1

            return cnt

        return bfs(0, adjlist)


s = Solution2()

k1 = s.reachableNodes(7, [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], [4, 5])

k2 = s.reachableNodes(7, [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]], [4, 2, 1])

print(k1)
print(k2)
