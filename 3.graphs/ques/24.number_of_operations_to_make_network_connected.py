# Number of operations to make network connected
"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming
a network where connections[i] = [ai, bi]
represents a connection between computers ai and bi.
Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections.
You can extract certain cables between two directly connected computers,
and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to
make all the computers connected. If it is not possible, return -1.
"""
"""
Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation:
Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
"""
"""
Constraints:
- 1 <= n <= 105
- 1 <= connections.length <= min(n * (n - 1) / 2, 105)
- connections[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no repeated connections.
- No two computers are connected by more than one cable.
"""


class DisjointSet:
    def __init__(self, V):
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
            return

        if self.sizes[ulp_u] < self.sizes[ulp_v]:
            self.parents[ulp_u] = ulp_v
            self.sizes[ulp_v] += self.sizes[ulp_u]
        else:
            self.parents[ulp_v] = ulp_u
            self.sizes[ulp_u] += self.sizes[ulp_v]


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1

        ds = DisjointSet(n)

        for u, v in connections:
            ds.unionBySizes(u, v)

        len_comp = len({ds.findUPar(i): 1 for i in range(n)})

        return len_comp - 1


s = Solution()

k1 = s.makeConnected(
    4,
    [
        [0, 1],
        [0, 2],
        [1, 2],
    ],
)

k2 = s.makeConnected(
    6,
    [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 2],
        [1, 3],
    ],
)

k3 = s.makeConnected(
    6,
    [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 2],
    ],
)

k4 = s.makeConnected(
    12,
    [
        [1, 5],
        [1, 7],
        [1, 2],
        [1, 4],
        [3, 7],
        [4, 7],
        [3, 5],
        [0, 6],
        [0, 1],
        [0, 4],
        [2, 6],
        [0, 3],
        [0, 2],
    ],
)

print(k1)
print(k2)
print(k3)
print(k4)
