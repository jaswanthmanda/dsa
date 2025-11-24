# Course Schedule I
"""
There are a total of N tasks, labeled from 0 to N-1.
Given an array arr where arr[i] = [a, b] indicates that you must take course
b first if you want to take course a.
Find if it is possible to finish all tasks.
"""

"""
Input: N = 4, arr = [[1,0],[2,1],[3,2]]
Output: True
Explanation:
It is possible to finish all the tasks in the order : 0 1 2 3.
First, we will finish task 0. Then we will finish task 1, task 2, and task 3.

Input: N = 4, arr = [[0,1],[3,2],[1,3],[3,0]]
Output: False
Explanation:
It is impossible to finish all the tasks. Let’s analyze the pairs:
- For pair {0, 1} -> we need to finish task 1 first and then task 0. (order : 1 0).
- For pair{3, 2} -> we need to finish task 2 first and then task 3. (order: 2 3).
- For pair {1, 3} -> we need to finish task 3 first and then task 1. (order: 3 1).
- But for pair {3, 0} -> we need to finish task 0 first and then
    task 3 but task 0 requires task 1 and task 1 requires task 3.
    So, it is not possible to finish all the tasks.
"""


class Solution:
    def canFinish(self, N, arr):
        # Build adjacency list
        adj = {i: [] for i in range(N)}
        for a, b in arr:
            adj[a].append(b)  # b -> a

        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:  # back-edge -> CYCLE
                return False

            if node in visited:  # already processed
                return True

            visiting.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            visiting.remove(node)
            visited.add(node)
            return True

        # Run DFS for all nodes (graph may be disconnected)
        for i in range(N):
            if not dfs(i):
                return False

        return True


s = Solution()

k1 = s.canFinish(
    4,
    [
        [1, 0],
        [2, 1],
        [3, 2],
    ],
)

k2 = s.canFinish(
    4,
    [
        [0, 1],
        [3, 2],
        [1, 3],
        [3, 0],
    ],
)

print(k1)
print(k2)
