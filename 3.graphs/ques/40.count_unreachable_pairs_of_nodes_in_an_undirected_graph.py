# Count unreachable pairs of nodes in an undirected graph
"""
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1.
You are given a 2D integer array edges where edges[i] = [ai, bi]
denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.
"""
"""
Example 1:
Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation:
There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.

Example 2:
Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation:
There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.
"""
"""
Constraints:
- 1 <= n <= 105
- 0 <= edges.length <= 2 * 105
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no repeated edges.
"""


class DisjointSet:
    def __init__(self, V):
        self.nodes = [i for i in range(V)]
        self.parents = [i for i in range(V)]
        self.sizes = [1 for i in range(V)]

    def findUPar(self, u):
        if u == self.parents[u]:
            return u

        self.parents[u] = self.findUPar(self.parents[u])

        return self.parents[u]

    def unionBySizes(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return 0

        if self.sizes[ulp_u] < self.sizes[ulp_v]:
            self.parents[ulp_u] = ulp_v
            self.sizes[ulp_v] += self.sizes[ulp_u]
        else:
            self.parents[ulp_v] = ulp_u
            self.sizes[ulp_u] += self.sizes[ulp_v]


class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ds = DisjointSet(n)

        for u, v in edges:
            ds.unionBySizes(u, v)

        item_map = {}

        for i in range(n):
            item = ds.findUPar(i)
            if item not in item_map:
                item_map[item] = 1
            else:
                item_map[item] += 1

        if len(item_map) == 1:
            return 0

        res = 0
        total_nodes = n

        for item in item_map:
            total_nodes -= item_map[item]
            res += item_map[item] * total_nodes

        return res


s = Solution()

k1 = s.countPairs(
    3,
    [
        [0, 1],
        [0, 2],
        [1, 2],
    ],
)

k2 = s.countPairs(
    7,
    [
        [0, 2],
        [0, 5],
        [2, 4],
        [1, 6],
        [5, 4],
    ],
)

print(k1)
print(k2)
