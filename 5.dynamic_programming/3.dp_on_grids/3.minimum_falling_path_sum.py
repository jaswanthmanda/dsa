# Minimum falling path sum
"""
Given a 2d array called matrix consisting of integer values.
Return the minimum path sum that can be obtained by starting
at any cell in the first row and ending at any cell in the last row.

Movement is allowed only to the bottom, bottom-right,
or bottom-left cell of the current cell.
"""

"""
Example 1:
Input: matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
Output: 6
Explanation:
One optimal route can be:-
Start at 1st cell of 1st row -> bottom-right -> bottom -> bottom-left.

Example 2:
Input: matrix = [[1, 4, 3, 1], [2, 3, -1, -1], [1, 1, -1, 8]]
Output: -1
Explanation:
One optimal route can be:-
Start at 4th cell of 1st row -> bottom-left -> bottom.
"""
"""
Constraints:
m == number of rows in matrix
n == number of columns in matrix
1 <= n, m <= 100
-1000 <= matrix[i][j] <= 1000
The answer will not exceed 109
"""


class Solution:
    def func(self, r, c, n, matrix, dp):
        if r < 0 or c < 0 or c >= n:
            return float("inf")

        if r == 0:
            return matrix[r][c]

        if dp[r][c] != -1:
            return dp[r][c]

        min_sum = float("inf")

        for i in range(c - 1, c + 2):
            min_sum = min(
                min_sum,
                self.func(
                    r - 1,
                    i,
                    n,
                    matrix,
                    dp,
                ),
            )

        dp[r][c] = matrix[r][c] + min_sum

        return dp[r][c]

    def minFallingPathSum(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dp = [[-1] * (n + 1) for _ in range(m)]

        min_sum = float("inf")

        for i in range(n):
            min_sum = min(min_sum, self.func(m - 1, i, n, matrix, dp))

        return min_sum


s = Solution()

k1 = s.minFallingPathSum(
    [
        [1, 2, 10, 4],
        [100, 3, 2, 1],
        [1, 1, 20, 2],
        [1, 2, 2, 1],
    ]
)

k2 = s.minFallingPathSum(
    [
        [1, 4, 3, 1],
        [2, 3, -1, -1],
        [1, 1, -1, 8],
    ]
)

print(k1)
print(k2)
