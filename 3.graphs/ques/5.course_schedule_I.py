# Course Schedule
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

- For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.
"""
"""
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation:
There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation:
There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and
to take course 0 you should also have finished course 1.
So it is impossible.
"""
"""
Constraints:
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build adj list
        adjList = {i: [] for i in range(numCourses)}

        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])

        visiting = set()
        visited = set()

        def dfs(start, adj):
            if start in visiting:
                return False

            if start in visited:
                return True

            visiting.add(start)

            for nei in adj[start]:
                if not dfs(nei, adj):
                    return False

            visiting.remove(start)
            visited.add(start)
            return True

        for i in range(numCourses):
            if not dfs(i, adjList):
                return False

        return True


s = Solution()

k1 = s.canFinish(
    2,
    [
        [1, 0],
    ],
)

k2 = s.canFinish(
    2,
    [
        [1, 0],
        [0, 1],
    ],
)

k3 = s.canFinish(1, [])

print(k1)
print(k2)
print(k3)
