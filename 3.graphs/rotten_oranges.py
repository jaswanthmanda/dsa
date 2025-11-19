from collections import deque

# Rotten Oranges
"""
Given an n x m grid, where each cell has the following values :



2 - represents a rotten orange

1 - represents a Fresh orange

0 - represents an Empty Cell

Every minute, if a fresh orange is adjacent to a rotten orange in 4-direction ( upward, downwards, right, and left ) it becomes rotten.



Return the minimum number of minutes required such that none of the cells has a Fresh Orange. If it's not possible, return -1.
"""

"""
Examples:
Input: grid = [ [2, 1, 1] , [0, 1, 1] , [1, 0, 1] ]
Output: -1
Explanation: Orange at (3,0) cannot be rotten.

Input: grid = [ [2,1,1] , [1,1,0] , [0,1,1] ]
Output: 4
"""


class Solution:
    def orangesRotting(self, grid):
        visited = set()
        m = len(grid)
        n = len(grid[0])
        q = deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 and (i, j) not in visited:
                    visited.add((i, j))
                    q.append((i, j, 0))

        maxTimer = 0
        while q:
            # while q[0][2] == timer:
            a, b, tc = q.popleft()
            if maxTimer < tc:
                maxTimer = tc

            vals = [
                (a, b - 1),
                (a, b + 1),
                (a - 1, b),
                (a + 1, b),
            ]

            for val in vals:
                c, d = val[0], val[1]
                if (
                    0 <= c < m
                    and 0 <= d < n
                    and grid[c][d] == 1
                    and (c, d) not in visited
                ):
                    grid[c][d] = 2
                    visited.add((c, d))
                    q.append((c, d, tc + 1))

            # timer += 1

        for aa in range(m):
            for ab in range(n):
                if grid[aa][ab] == 1:
                    return -1

        return maxTimer


"""
Wrong Answer
970ms
51.15MB
Grid
[[2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1],[1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0],[1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1],[0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1],[1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2],[1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1],[0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1],[1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0],[1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1],[2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1],[1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0],[1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1],[0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1],[1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2],[1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1],[0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1],[1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0],[1,1,2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1],[2,1,1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1],[1,0,1,1,0,1,1,2,1,1,0,1,1,0,1,1,2,1,1,0]]
Your Output
4
Expected Output
3
"""

s = Solution()

k1 = s.orangesRotting(
    [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1],
    ]
)

k2 = s.orangesRotting(
    [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
)

k3 = s.orangesRotting(
    [
        [2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1],
        [1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0],
        [1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1],
        [0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1],
        [1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2],
        [1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1],
        [0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1],
        [1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0],
        [1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1],
        [2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1],
        [1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0],
        [1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1],
        [0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1],
        [1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2],
        [1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1],
        [0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1],
        [1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0],
        [1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1],
        [2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1],
        [1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 0, 1, 1, 2, 1, 1, 0],
    ]
)

print(k1)
print(k2)
print(k3)
