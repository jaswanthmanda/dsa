#  Most stones removed with same row or column
"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents
the location of the ith stone, return the largest possible number of stones that can be removed.
"""
"""
Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation:
One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.


Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation:
One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.


Example 3:
Input: stones = [[0,0]]
Output: 0
[0,0] is the only stone on the plane, so you cannot remove it.
"""
"""
Constraints:
- 1 <= stones.length <= 1000
- 0 <= xi, yi <= 104
- No two stones are at the same coordinate point.
"""


class DisjointSet:
    def __init__(self, V):
        self.nodes = [i for i in range(V)]
        self.parent = [i for i in range(V)]
        self.sizes = [1 for i in range(V)]

    def findUPar(self, u):
        print(u, len(self.parent))
        if u == self.parent[u]:
            return u

        self.parent[u] = self.findUPar(self.parent[u])

        return self.parent[u]

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        if self.sizes[ulp_u] < self.sizes[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.sizes[ulp_v] += self.sizes[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.sizes[ulp_u] += self.sizes[ulp_v]


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        maxRow = 0
        maxCol = 0
        for edge in stones:
            maxRow = max(edge[0], maxRow)
            maxCol = max(edge[1], maxCol)

        ds = DisjointSet(maxRow + maxCol + 2)
        map = {}

        for edge in stones:
            nodeRow = edge[0]
            nodeCol = edge[1] + maxRow + 1

            ds.unionBySize(nodeRow, nodeCol)
            map[nodeRow] = 1
            map[nodeCol] = 1

        cnt = 0
        for item in map.keys():
            if ds.findUPar(item) == item:
                cnt += 1

        return len(stones) - cnt


s = Solution()

k1 = s.removeStones(
    [
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 2],
        [2, 1],
        [2, 2],
    ]
)

k2 = s.removeStones(
    [
        [0, 0],
        [0, 2],
        [1, 1],
        [2, 0],
        [2, 2],
    ]
)

k3 = s.removeStones(
    [
        [0, 0],
    ]
)

k4 = s.removeStones(
    [
        [3, 3],
        [4, 4],
        [1, 4],
        [1, 5],
        [2, 3],
        [4, 3],
        [2, 4],
    ]
)

print(k1)
print(k2)
print(k3)
print(k4)
