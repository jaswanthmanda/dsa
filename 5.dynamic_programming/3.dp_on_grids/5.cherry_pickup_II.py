import copy

# Cherry Pickup II
"""
Given a n x m 2d integer array called matrix where matrix[i][j] represents the number of cherries you can pick up from the (i, j) cell.
Given two robots that can collect cherries, one is located at the top-leftmost (0, 0) cell and the other at the top-rightmost (0, m-1) cell.

Return the maximum number of cherries that can be picked by the two robots in total, following these rules:

Robots that are standing on (i, j) cell can only move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1), if it exists in the matrix.

A robot will pick up all the cherries in a given cell when it passes through that cell.

If both robots come to the same cell at the same time, only one robot takes the cherries.

Both robots must reach the bottom row in matrix.
"""
"""
Example 1:
Input: matrix = [[2, 1, 3], [4, 2, 5], [1, 6, 2], [7, 2, 8]]
Output: 37
Explanation:
Possible left robot path:-
Start at 0th cell (2) -> down (4) -> down-right (6) ->down-left (7)
Possible right robot path:-
Start at 2nd cell (3) -> down (5) -> down (2) -> down (8)


Example 2:
Input: matrix = [[1, 4, 4, 1], [1, 2, 2, 1], [5, 6, 10, 11], [8, 1, 1, 1]]
Output: 32
Explanation:
Possible left robot path:-
Start at 0th cell (1) -> down-right (2) -> down (6) ->down-left (8)
Possible right robot path:-
Start at 3rd cell (1) -> down-left (2) -> down-right (11) -> down (1)
"""
"""
Constraints
- n == number of rows in matrix
- m == number of columns in matrix
- 2 <= n, m <= 70
- 0 <= matrix[i][j] <= 1000
"""


# brute force
class Solution:
    def func(self, i, j1, j2, matrix, dp):
        if j1 < 0 or j2 < 0 or j1 >= len(matrix[0]) or j2 >= len(matrix[0]):
            return float("-inf")

        if i == len(matrix) - 1:
            if j1 == j2:
                return matrix[i][j1]
            return matrix[i][j1] + matrix[i][j2]

        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        maxi = float("-inf")

        for dj1 in range(-1, 2):
            for dj2 in range(-1, 2):
                if j1 == j2:
                    value = matrix[i][j1]
                else:
                    value = matrix[i][j1] + matrix[i][j2]

                value += self.func(
                    i + 1,
                    j1 + dj1,
                    j2 + dj2,
                    matrix,
                    dp,
                )

                maxi = max(maxi, value)

        dp[i][j1][j2] = maxi

        return dp[i][j1][j2]

    def cherryPickup(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(m)]

        return self.func(0, 0, n - 1, matrix, dp)


class SolutionOptimal:
    def cherryPickup(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(m)]

        for j1 in range(0, n):
            for j2 in range(0, n):
                if j1 == j2:
                    dp[m - 1][j1][j2] = matrix[m - 1][j1]
                else:
                    dp[m - 1][j1][j2] = matrix[m - 1][j1] + matrix[m - 1][j2]

        for i in range(m - 2, -1, -1):
            for j1 in range(n):
                for j2 in range(n):
                    maxi = float("-inf")
                    for dj1 in range(-1, 2):
                        for dj2 in range(-1, 2):
                            if j1 == j2:
                                value = matrix[i][j1]
                            else:
                                value = matrix[i][j1] + matrix[i][j2]

                            if (
                                j1 + dj1 >= 0
                                and j1 + dj1 < n
                                and j2 + dj2 >= 0
                                and j2 + dj2 < n
                            ):
                                value += dp[i + 1][j1 + dj1][j2 + dj2]
                            else:
                                value += float("-inf")

                            maxi = max(maxi, value)

                    dp[i][j1][j2] = maxi

        return dp[0][0][n - 1]


class SolutionOptimalSpace:
    def cherryPickup(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        front = [[0] * (n + 1) for _ in range(n)]
        curr = [[0] * (n + 1) for _ in range(n)]

        for j1 in range(0, n):
            for j2 in range(0, n):
                if j1 == j2:
                    front[j1][j2] = matrix[m - 1][j1]
                else:
                    front[j1][j2] = matrix[m - 1][j1] + matrix[m - 1][j2]

        for i in range(m - 2, -1, -1):
            curr = [[0] * (n + 1) for _ in range(n)]
            for j1 in range(n):
                for j2 in range(n):
                    maxi = float("-inf")
                    for dj1 in range(-1, 2):
                        for dj2 in range(-1, 2):
                            if j1 == j2:
                                value = matrix[i][j1]
                            else:
                                value = matrix[i][j1] + matrix[i][j2]

                            if (
                                j1 + dj1 >= 0
                                and j1 + dj1 < n
                                and j2 + dj2 >= 0
                                and j2 + dj2 < n
                            ):
                                value += front[j1 + dj1][j2 + dj2]
                            else:
                                value += float("-inf")

                            maxi = max(maxi, value)

                    curr[j1][j2] = maxi

            front, curr = curr, front

        return front[0][n - 1]


s = SolutionOptimalSpace()

k1 = s.cherryPickup(
    [
        [2, 1, 3],
        [4, 2, 5],
        [1, 6, 2],
        [7, 2, 8],
    ]
)

k2 = s.cherryPickup(
    [
        [1, 4, 4, 1],
        [1, 2, 2, 1],
        [5, 6, 10, 11],
        [8, 1, 1, 1],
    ]
)

print(k1)
print(k2)
