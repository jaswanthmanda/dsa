import copy

# Course Schedule V
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course ai first if you want to take course bi.

- For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.

Prerequisites can also be indirect. If course a is
a prerequisite of course b, and course b
is a prerequisite of course c, then course a is a prerequisite of course c.

Prerequisites can also be indirect. If course
a is a prerequisite of course b, and course b is
a prerequisite of course c, then course a is a prerequisite of course c.

Return a boolean array answer, where answer[j] is the answer to the jth query.
"""
"""
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation:
The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

Example 2:
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation:
There are no prerequisites, and each course is independent.

Example 3:
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
"""
"""
Constraints:
- 2 <= numCourses <= 100
- 0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
- prerequisites[i].length == 2
- 0 <= ai, bi <= numCourses - 1
- ai != bi
- All the pairs [ai, bi] are unique.
- The prerequisites graph has no cycles.
- 1 <= queries.length <= 104
- 0 <= ui, vi <= numCourses - 1
- ui != vi
"""


class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Floyd-Warshall to get reachable from preq: a -> c (query: a -> b -> c)

        reachable = [[False] * numCourses for _ in range(numCourses)]

        for u, v in prerequisites:
            reachable[u][v] = True

        for k in range(numCourses):
            for i in range(numCourses):
                if reachable[i][k]:
                    for j in range(numCourses):
                        if reachable[k][j]:
                            reachable[i][j] = True

        return [reachable[u][v] for u, v in queries]


s = Solution()

k1 = s.checkIfPrerequisite(
    2,
    [
        [1, 0],
    ],
    [
        [0, 1],
        [1, 0],
    ],
)

k2 = s.checkIfPrerequisite(
    2,
    [],
    [
        [1, 0],
        [0, 1],
    ],
)

k3 = s.checkIfPrerequisite(
    3,
    [
        [1, 2],
        [1, 0],
        [2, 0],
    ],
    [
        [1, 0],
        [1, 2],
    ],
)

k4 = s.checkIfPrerequisite(
    4,
    [[2, 3], [2, 1], [0, 3], [0, 1]],
    [[0, 1], [0, 3], [2, 3], [3, 0], [2, 0], [0, 2]],
)

print(k1)
print(k2)
print(k3)
print(k4)
