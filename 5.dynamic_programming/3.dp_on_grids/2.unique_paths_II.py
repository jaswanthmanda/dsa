# Unique paths II
"""
Given an m x n 2d array named matrix, where each cell is either 0 or 1.
Return the number of unique ways to go from the
top-left cell (matrix[0][0]) to the bottom-right cell (matrix[m-1][n-1]).
A cell is blocked if its value is 1, and no path is possible through that cell.

Movement is allowed in only two directions from a cell - right and bottom.
"""
"""
Example 1
Input: matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
Output: 2
Explanation:
The two possible paths are:
1) down -> down-> right -> right
2) right -> right -> down -> down


Example 2:
Input: matrix = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
Output: 0
Explanation:
There is no way to reach the bottom-right cell.
"""
"""
Constraints:
m == number of rows in matrix
n == number of columns in matrix
1 <= n, m <= 100
Value of each cell in matrix is either 0 or 1
The answer will not exceed 109
"""


class Solution:
    def func(self, r, c, matrix, dp):
        if r < 0 or c < 0:
            return 0

        if matrix[r][c] == 1:
            return 0

        if r == 0 and c == 0:
            return 1

        if dp[r][c] != -1:
            return dp[r][c]

        up = self.func(r - 1, c, matrix, dp)
        left = self.func(r, c - 1, matrix, dp)

        dp[r][c] = up + left

        return up + left

    def uniquePathsWithObstacles(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dp = [[-1] * (n + 1) for _ in range(m)]

        return self.func(
            m - 1,
            n - 1,
            matrix,
            dp,
        )


s = Solution()

k1 = s.uniquePathsWithObstacles(
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
)

k2 = s.uniquePathsWithObstacles(
    [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
    ]
)

print(k1)
print(k2)
