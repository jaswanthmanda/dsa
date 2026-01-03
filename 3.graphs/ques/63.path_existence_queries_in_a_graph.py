# Path existence queries in a graph
"""
You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.

You are also given an integer array nums of length n sorted in non-decreasing order, and an integer maxDiff.

An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).

You are also given a 2D integer array queries. For each queries[i] = [ui, vi], determine whether there exists a path between nodes ui and vi.

Return a boolean array answer, where answer[i] is true if there exists a path between ui and vi in the ith query and false otherwise.
"""
"""
Example 1:
Input: n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]
Output: [true,false]
Explanation:
- Query [0,0]: Node 0 has a trivial path to itself.
- Query [0,1]: There is no edge between Node 0 and Node 1 because |nums[0] - nums[1]| = |1 - 3| = 2, which is greater than maxDiff.
- Thus, the final answer after processing all the queries is [true, false].


Example 2:
Input: n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]
Output: [false,false,true,true]
Explanation:
The resulting graph is:

- Query [0,1]: There is no edge between Node 0 and Node 1 because |nums[0] - nums[1]| = |2 - 5| = 3, which is greater than maxDiff.
- Query [0,2]: There is no edge between Node 0 and Node 2 because |nums[0] - nums[2]| = |2 - 6| = 4, which is greater than maxDiff.
- Query [1,3]: There is a path between Node 1 and Node 3 through Node 2 since |nums[1] - nums[2]| = |5 - 6| = 1 and |nums[2] - nums[3]| = |6 - 8| = 2, both of which are within maxDiff.
- Query [2,3]: There is an edge between Node 2 and Node 3 because |nums[2] - nums[3]| = |6 - 8| = 2, which is equal to maxDiff.
- Thus, the final answer after processing all the queries is [false, false, true, true].
"""
"""
Constraints:
- 1 <= n == nums.length <= 105
- 0 <= nums[i] <= 105
- nums is sorted in non-decreasing order.
- 0 <= maxDiff <= 105
- 1 <= queries.length <= 105
- queries[i] == [ui, vi]
- 0 <= ui, vi < n
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
            return None

        if self.sizes[ulp_u] <= self.sizes[ulp_v]:
            self.parents[ulp_u] = ulp_v
            self.sizes[ulp_v] += self.sizes[ulp_u]
        else:
            self.parents[ulp_v] = ulp_u
            self.sizes[ulp_u] += self.sizes[ulp_v]


class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        ds = DisjointSet(n)

        for i in range(n):
            if abs(nums[i] - nums[i - 1]) <= maxDiff:
                ds.unionBySizes(i - 1, i)

        # simple for loop
        result = []

        for u, v in queries:
            if u == v:
                result.append(True)
            elif ds.findUPar(u) == ds.findUPar(v):
                result.append(True)
            else:
                result.append(False)

        # return result
        return result


s = Solution()

k1 = s.pathExistenceQueries(
    2,
    [1, 3],
    1,
    [
        [0, 0],
        [0, 1],
    ],
)

k2 = s.pathExistenceQueries(
    4,
    [2, 5, 6, 8],
    2,
    [
        [0, 1],
        [0, 2],
        [1, 3],
        [2, 3],
    ],
)

print(k1)
print(k2)
