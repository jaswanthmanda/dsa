# Maximal network rank
"""
There is an infrastructure of n cities with some number of roads connecting these cities.
Each roads[i] = [ai, bi] indicates that
there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total
number of directly connected roads to either city.
If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
"""
"""
Example 1:
Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation:
The network rank of cities 0 and 1 is 4 as there are 4 roads
that are connected to either 0 or 1.
The road between 0 and 1 is only counted once.

Example 2:
Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation:
There are 5 roads that are connected to cities 1 or 2.

Example 3:
Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation:
The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
"""
"""
Constraints:
- 2 <= n <= 100
- 0 <= roads.length <= n * (n - 1) / 2
- roads[i].length == 2
- 0 <= ai, bi <= n-1
- ai != bi
- Each pair of cities has at most one road connecting them.
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
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        ds = DisjointSet(n)

        for edge in roads:
            ds.unionBySizes(edge[0], edge[1])

        # print(ds.sizes)

        return max(ds.sizes)


s = Solution()

k1 = s.maximalNetworkRank(
    4,
    [
        [0, 1],
        [0, 3],
        [1, 2],
        [1, 3],
    ],
)

k2 = s.maximalNetworkRank(
    5,
    [
        [0, 1],
        [0, 3],
        [1, 2],
        [1, 3],
        [2, 3],
        [2, 4],
    ],
)

k3 = s.maximalNetworkRank(
    8,
    [
        [0, 1],
        [1, 2],
        [2, 3],
        [2, 4],
        [5, 6],
        [5, 7],
    ],
)

print(k1)
print(k2)
print(k3)
