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

        def bfs(a, b):
            q = deque([(a, b)])
            visited.add((a, b))
            minut = 0

            while q:
                c, d = q.popleft()

                vals = [
                    (c - 1, d),
                    (c + 1, d),
                    (c, d - 1),
                    (c, d + 1),
                ]

                found = False

                for val in vals:
                    row = val[0]
                    col = val[1]
                    if (
                        0 <= row < m
                        and 0 <= col < n
                        and grid[row][col] == 1
                        and (row, col) not in visited
                    ):
                        grid[row][col] = 2
                        visited.add((row, col))
                        q.append((row, col))

                        if not found:
                            found = True

                if (c, d) != (a, b) and found:
                    minut += 1

            return minut

        minCounter = 501

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 and (i, j) not in visited:
                    counter = bfs(i, j)
                    if counter != 0 and minCounter > counter:
                        minCounter = counter

        for aa in range(m):
            for ab in range(n):
                if grid[aa][ab] == 1:
                    return -1

        return minCounter


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
