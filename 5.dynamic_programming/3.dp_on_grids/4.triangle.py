# Triangle
"""
Given a 2d integer array named triangle with n rows.
Its first row has 1 element and each succeeding row has one more element in it than the row above it.

Return the minimum falling path sum from the first row to the last.

Movement is allowed only to the bottom or bottom-right cell from the current cell.
"""
"""
Example 1:
Input: triangle = [[1], [1, 2], [1, 2, 4]]
Output: 3
Explanation:
One possible route can be:
Start at 1st row -> bottom -> bottom.

Example 2:
Input: triangle = [[1], [4, 7], [4,10, 50], [-50, 5, 6, -100]]
Output: -42
Explanation:
One possible route can be:
Start at 1st row -> bottom-right -> bottom-right -> bottom-right
"""
"""
Constraints
n == number of rows in triangle
1 <= n <= 200
-104 <= triangle[i][j] <= 104
triangle[0].length == 1
triangle[i].length = triangle[i-1].length + 1
The answer will not exceed 109
"""


class Solution:
    def func(self, i, j, matrix, dp):
        if i < 0 or j < 0 or j >= len(matrix[i]):
            return float("inf")

        if i == 0:
            return matrix[0][j]

        if dp[i][j] != -1:
            return dp[i][j]

        u = matrix[i][j] + self.func(i - 1, j, matrix, dp)
        v = matrix[i][j] + self.func(i - 1, j - 1, matrix, dp)

        dp[i][j] = min(u, v)

        return dp[i][j]

    def minTriangleSum(self, triangle):
        m = len(triangle)
        n = len(triangle[m - 1])

        maxi = float("inf")

        dp = [[-1] * (len(triangle[i]) + 1) for i in range(m)]

        for i in range(n - 1, -1, -1):
            maxi = min(maxi, self.func(m - 1, i, triangle, dp))

        return maxi


class SolutionOptimal:
    def minTriangleSum(self, triangle):
        m = len(triangle)
        n = len(triangle[m - 1])

        prev = [triangle[0][0]]

        for i in range(1, m):
            curr = [0] * (len(triangle[i]))
            for j in range(len(triangle[i])):
                if j >= len(prev):
                    u = float("inf")
                else:
                    u = triangle[i][j] + prev[j]

                if j - 1 < 0:
                    v = float("inf")
                else:
                    v = triangle[i][j] + prev[j - 1]

                curr[j] = min(u, v)

            prev = curr

        mini = float("inf")
        for i in range(n):
            mini = min(mini, prev[i])

        return mini


s = SolutionOptimal()

k1 = s.minTriangleSum(
    [
        [1],
        [1, 2],
        [1, 2, 4],
    ]
)

k2 = s.minTriangleSum(
    [
        [1],
        [4, 7],
        [4, 10, 50],
        [-50, 5, 6, -100],
    ]
)

print(k1)
print(k2)
