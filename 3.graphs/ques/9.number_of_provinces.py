from collections import deque

# Number of provinces
"""
There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b,
and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith
city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""
"""
Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

[[1,1,0],
 [1,1,0],
 [0,0,1]]

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""
"""
Constraints:
- 1 <= n <= 200
- n == isConnected.length
- n == isConnected[i].length
- isConnected[i][j] is 1 or 0.
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]
"""


class Solution(object):
    def bfs(self, start, adjList):
        q = deque([start])
        self.visited.add(start)

        while q:
            node = q.popleft()

            for nei in adjList[node]:
                if nei not in self.visited:
                    self.visited.add(nei)
                    q.append(nei)

    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)

        # build adjlist
        adjList = {i: [] for i in range(n)}

        for i in range(n):
            for j in range(n):
                if i < j and isConnected[i][j] == 1:
                    adjList[i].append(j)
                    adjList[j].append(i)

        self.visited = set()
        component = 0
        for i in range(n):
            if i not in self.visited:
                self.bfs(i, adjList)
                component += 1

        return component


s = Solution()

k1 = s.findCircleNum(
    [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1],
    ]
)

k2 = s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# edge cases

k3 = s.findCircleNum([[1]])
k4 = s.findCircleNum(
    [
        [1, 0],
        [0, 1],
    ]
)

# missed case
k5 = s.findCircleNum(
    [
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1],
    ]
)

print(k1)
print(k2)
print(k3)
print(k4)
print(k5)
