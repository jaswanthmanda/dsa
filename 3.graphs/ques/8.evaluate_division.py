from collections import deque

# Evaluate Division
"""
You are given an array of variable pairs equations and an array of real numbers values,
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj]
represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid.
You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
"""
"""
Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""
"""
Constraints:
- 1 <= equations.length <= 20
- equations[i].length == 2
- 1 <= Ai.length, Bi.length <= 5
- values.length == equations.length
- 0.0 < values[i] <= 20.0
- 1 <= queries.length <= 20
- queries[i].length == 2
- 1 <= Cj.length, Dj.length <= 5
- Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""


class Solution(object):
    def bfs(self, start, dest, adjList):
        # print(start, dest, start not in adjList or dest not in adjList)
        if dest not in adjList or start not in adjList:
            # print("came here 1")
            return format(-1, ".5f")

        if start == dest:
            return format(1, ".5f")

        pq = deque([(start, 1)])
        visited = set([start])

        while pq:
            node, distNode = pq.popleft()

            if node not in adjList:
                continue

            for nei, dist_nei in adjList[node]:
                if nei not in visited:
                    kas = distNode * dist_nei

                    if nei == dest:
                        return format(kas, ".5f")

                    visited.add(nei)
                    pq.append((nei, kas))

        return format(-1, ".5f")

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # build adj list
        adjList = {}

        for i, edge in enumerate(equations):
            if edge[0] not in adjList:
                adjList[edge[0]] = []
            if edge[1] not in adjList:
                adjList[edge[1]] = []

            adjList[edge[0]].append((edge[1], values[i]))
            adjList[edge[1]].append((edge[0], 1 / values[i]))

        ans = [format(-1, ".5f") for _ in range(len(queries))]
        for i, query in enumerate(queries):
            ans[i] = self.bfs(query[0], query[1], adjList)
            ans[i] = float(ans[i])

        return ans


s = Solution()

k1 = s.calcEquation(
    [
        ["a", "b"],
        ["b", "c"],
    ],
    [2.0, 3.0],
    [
        ["a", "c"],
        ["b", "a"],
        ["a", "e"],
        ["a", "a"],
        ["x", "x"],
    ],
)

k2 = s.calcEquation(
    [
        ["a", "b"],
        ["b", "c"],
        ["bc", "cd"],
    ],
    [
        1.5,
        2.5,
        5.0,
    ],
    [
        ["a", "c"],
        ["c", "b"],
        ["bc", "cd"],
        ["cd", "bc"],
    ],
)

k3 = s.calcEquation(
    [
        ["a", "b"],
    ],
    [0.5],
    [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]],
)

k4 = s.calcEquation(
    [["a", "e"], ["b", "e"]],
    [4.0, 3.0],
    [
        ["a", "b"],
        ["e", "e"],
        ["x", "x"],
    ],
)

print(k1)
print(k2)
print(k3)
print(k4)
