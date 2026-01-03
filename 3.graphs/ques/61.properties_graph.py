# Properties graph
"""
You are given a 2D integer array properties having dimensions n x m and an integer k.

Define a function intersect(a, b) that returns the number of distinct integers common to both arrays a and b.

Construct an undirected graph where each index i corresponds to properties[i].
There is an edge between node i and node j if and only if intersect(properties[i], properties[j]) >= k,
where i and j are in the range [0, n - 1] and i != j.

Return the number of connected components in the resulting graph.
"""
"""
Example 1:
Input: properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1
Output: 3
Explanation:
The graph formed has 3 connected components:

Example 2:
Input: properties = [[1,2,3],[2,3,4],[4,3,5]], k = 2
Output: 1
Explanation:
The graph formed has 1 connected component:


Example 3:
Input: properties = [[1,1],[1,1]], k = 2
Output: 2
Explanation:
intersect(properties[0], properties[1]) = 1, which is less than k.
This means there is no edge between properties[0] and properties[1] in the graph.
"""
"""
Constraints:
- 1 <= n == properties.length <= 100
- 1 <= m == properties[i].length <= 100
- 1 <= properties[i][j] <= 100
- 1 <= k <= m
"""


class DisjointSet:
    def __init__(self, V):
        self.nodes = [i for i in range(V)]
        self.parents = [i for i in range(V)]
        self.sizes = [1 for _ in range(V)]

    def findUPar(self, u):
        if u == self.parents[u]:
            return u

        self.parents[u] = self.findUPar(self.parents[u])

        return self.parents[u]

    def unionBySizes(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return None

        if self.sizes[ulp_u] < self.sizes[ulp_v]:
            self.parents[ulp_u] = ulp_v
            self.sizes[ulp_v] += self.sizes[ulp_u]
        else:
            self.parents[ulp_v] = ulp_u
            self.sizes[ulp_u] += self.sizes[ulp_v]


class Solution(object):
    def numberOfComponents(self, properties, k):
        """
        :type properties: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(properties)

        sets = [set(row) for row in properties]

        dsu = DisjointSet(n)

        for i in range(n):
            for j in range(i + 1, n):
                if len(sets[i] & sets[j]) >= k:
                    dsu.unionBySizes(i, j)

        # Count unique parents
        parents = set([dsu.findUPar(i) for i in range(n)])
        return len(parents)


s = Solution()

k1 = s.numberOfComponents(
    [
        [1, 2],
        [1, 1],
        [3, 4],
        [4, 5],
        [5, 6],
        [7, 7],
    ],
    1,
)

k2 = s.numberOfComponents(
    [
        [1, 2, 3],
        [2, 3, 4],
        [4, 3, 5],
    ],
    2,
)

k3 = s.numberOfComponents(
    [
        [1, 1],
        [1, 1],
    ],
    2,
)

print(k1)
print(k2)
print(k3)
