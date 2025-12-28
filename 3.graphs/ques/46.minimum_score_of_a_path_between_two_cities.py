# Minimum score of a path between two cities
"""
You are given a positive integer n representing n cities numbered from 1 to n.
You are also given a 2D array roads
where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional
road between cities ai and bi with a distance equal to distancei.
The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:
- A path is a sequence of roads between two cities.
- It is allowed for a path to contain the same road multiple times, and you can visit
 cities 1 and n multiple times along the path.
- The test cases are generated such that there is at least one path between 1 and n.
"""
"""
Example 1:
Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation:
The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

Example 2:
Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation:
The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
"""
"""
Constraints:
- 2 <= n <= 105
- 1 <= roads.length <= 105
- roads[i].length == 3
- 1 <= ai, bi <= n
- ai != bi
- 1 <= distancei <= 104
- There are no repeated edges.
- There is at least one path between 1 and n.
"""


class DisjointSet:
    def __init__(self, V):
        self.nodes = [i for i in range(V + 1)]
        self.parents = [i for i in range(V + 1)]
        self.sizes = [1 for i in range(V + 1)]

    def findUPar(self, u):
        if u == self.parents[u]:
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
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        ds = DisjointSet(n)

        for u, v, _ in roads:
            ds.unionBySizes(u, v)

        strt_par = ds.findUPar(1)
        end_par = ds.findUPar(n)

        min_val = float("inf")

        for u, v, z in roads:
            if strt_par == end_par == ds.findUPar(u):
                min_val = min(min_val, z)

        return min_val


s = Solution()

k1 = s.minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]])

k2 = s.minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]])

print(k1)
print(k2)
