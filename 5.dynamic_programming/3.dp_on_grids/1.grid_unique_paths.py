# Grid unique paths
"""
Given two integers m and n, representing the number of rows and columns of a 2d array named matrix.
Return the number of unique ways to go from the top-left cell
(matrix[0][0]) to the bottom-right cell (matrix[m-1][n-1]).

Movement is allowed only in two directions from a cell: right and bottom.
"""
"""
Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
There are 3 unique ways to go from the top left to the bottom right cell.
1) right -> down -> down
2) down -> right -> down
3) down -> down -> right


Example 2:
Input: m = 2, n = 4
Output: 4
Explanation:
There are 4 unique ways to go from the top left to the bottom right cell.
1) down -> right -> right -> right
2) right -> down -> right -> right
3) right -> right -> down -> right
4) right -> right -> right -> down
"""


class Solution:
    def func(self, r, c, dp):
        if r == 0 and c == 0:
            return 1
        if r < 0 or c < 0:
            return 0

        if dp[r][c] != -1:
            return dp[r][c]

        up = self.func(r - 1, c, dp)
        left = self.func(r, c - 1, dp)

        dp[r][c] = up + left

        return dp[r][c]

    def uniquePaths(self, m, n):
        dp = [[-1] * n for _ in range(m)]

        for i in range(n):
            dp[0][i] = 1

        return self.func(m - 1, n - 1, dp)


class SolutionOptimal:
    def uniquePaths(self, m, n): ...


s = Solution()

k1 = s.uniquePaths(3, 2)

k2 = s.uniquePaths(2, 4)

print(k1)
print(k2)
