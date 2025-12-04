# Find the town judge
"""
In a town, there are n people labeled from 1 to n.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person
labeled ai trusts the person labeled bi.
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
"""
"""
Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
"""
"""
Constraints:
- 1 <= n <= 1000
- 0 <= trust.length <= 104
- trust[i].length == 2
- All the pairs of trust are unique.
- ai != bi
- 1 <= ai, bi <= n
"""


class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust) == 0:
            return -1

        if n < 2:
            return 1

        adj = {i: [] for i in range(1, n + 1)}

        in_map = {}
        # out_map = {}

        for edge in trust:
            adj[edge[0]].append(edge[1])

            if edge[1] not in in_map:
                in_map[edge[1]] = 1
            else:
                in_map[edge[1]] += 1

        for i in range(1, n + 1):
            if i in in_map and in_map[i] == n - 1 and adj[i] == []:
                return i

        return -1


# Optimal
class SolutionOptimal(object):
    def findJudge(self, n, trust):
        if len(trust) == 0:
            return 1 if n == 1 else -1

        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)

        for a, b in trust:
            out_degree[a] += 1
            in_degree[b] += 1

        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i

        return -1


s = Solution()

k1 = s.findJudge(
    2,
    [
        [1, 2],
    ],
)

k2 = s.findJudge(
    3,
    [
        [1, 3],
        [2, 3],
    ],
)

k3 = s.findJudge(
    3,
    [
        [1, 3],
        [2, 3],
        [3, 1],
    ],
)

print(k1)
print(k2)
print(k3)
