import heapq

# Maximum star sum of a graph
"""
There is an undirected graph consisting of n nodes numbered from 0 to n - 1. You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node.

You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A star graph is a subgraph of the given graph having a center node containing 0 or more neighbors. In other words, it is a subset of edges of the given graph such that there exists a common node for all edges.

The image below shows star graphs with 3 and 4 neighbors respectively, centered at the blue node.


The star sum is the sum of the values of all the nodes present in the star graph.

Given an integer k, return the maximum star sum of a star graph containing at most k edges.
"""
"""
Example 1:
Input: vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2
Output: 16
Explanation:
The above diagram represents the input graph.
The star graph with the maximum star sum is denoted by blue. It is centered at 3 and includes its neighbors 1 and 4.
It can be shown it is not possible to get a star graph with a sum greater than 16.

Example 2:
Input: vals = [-5], edges = [], k = 0
Output: -5
Explanation:
There is only one possible star graph, which is node 0 itself.
Hence, we return -5.
"""
"""
Constraints:
- n == vals.length
- 1 <= n <= 105
- -104 <= vals[i] <= 104
- 0 <= edges.length <= min(n * (n - 1) / 2, 105)
- edges[i].length == 2
- 0 <= ai, bi <= n - 1
- ai != bi
- 0 <= k <= n - 1
"""


class Solution(object):
    def maxStarSum(self, vals, edges, k):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not edges:
            return max(vals)

        # n
        n = len(vals)

        # build adjlist
        adjlist = {i: [] for i in range(n)}
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        self.max_val = max(vals)

        for i in range(n):
            chavu_motha = [vals[ii] for ii in adjlist[i]]

            og = sorted(chavu_motha, reverse=True)

            val = vals[i]

            for i in range(min(k, len(og))):
                if og[i] < 0:
                    break
                else:
                    val += og[i]

            self.max_val = max(self.max_val, val)

        return self.max_val


class SolutionOptimal:
    def maxStarSum(self, vals, edges, k):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not edges:
            return max(vals)

        # n
        n = len(vals)

        # build adjlist
        adjlist = {i: [] for i in range(n)}
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        max_val = max(vals)

        for i in range(n):
            best = heapq.nlargest(k, (vals[j] for j in adjlist[i]))

            curr = vals[i]
            for x in best:
                if x > 0:
                    curr += x

            max_val = max(max_val, curr)

        return max_val


s = SolutionOptimal()

k1 = s.maxStarSum(
    [1, 2, 3, 4, 10, -10, -20],
    [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [3, 6]],
    2,
)

k2 = s.maxStarSum([-5], [], 0)

print(k1)
print(k2)
