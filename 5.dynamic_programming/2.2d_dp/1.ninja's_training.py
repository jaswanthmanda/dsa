# Ninja's training
"""
A ninja has planned a n-day training schedule. Each day he has to perform one of three activities
-
running,
stealth tranetwining,
or fighting practice.
The same activity cannot be done on two consecutive
days and the ninja earns a specific number of merit points,
based on the activity and the given day.

Given a n x 3-sized matrix, where matrix[i][0], matrix[i][1], and matrix[i][2],
represent the merit points associated with running,
stealth and fighting practice, on the (i+1)th day respectively.
Return the maximum possible merit points that the ninja can earn.
"""
"""
Example 1
Input: matrix = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
Output: 210
Explanation:
Day 1: fighting practice = 70
Day 2: stealth training = 50
Day 3: fighting practice = 90
Total = 70 + 50 + 90 = 210
This gives the optimal points.

Example 2:
Input: matrix = [[70, 40, 10], [180, 20, 5], [200, 60, 30]]
Output: 290
Explanation:
Day 1: running = 70
Day 2: stealth training = 20
Day 3: running = 200
Total = 70 + 20 + 200 = 290
This gives the optimal points.
"""
"""
Constraints:
- 1 <= n <= 104
- n == number of rows in matrix
- 3 == number of columns in matrix
- 0 <= matrix[i][j] <= 1000
"""


class Solution:
    def func(self, ind, last, matrix, dp):
        if ind == 0:
            maxi_0 = float("-inf")

            for i in range(3):
                if i != last:
                    maxi_0 = max(maxi_0, matrix[ind][i])

            return maxi_0

        # if last < n:
        if dp[ind][last] != -1:
            return dp[ind][last]

        maxi = float("-inf")

        for i in range(3):
            if i != last:
                maxi = max(
                    maxi, matrix[ind][i] + self.func(ind - 1, i, matrix, dp)
                )

        # if last < 3:
        dp[ind][last] = maxi

        return dp[ind][last]

    def ninjaTraining(self, matrix):
        n = len(matrix)

        dp = [[-1] * 4 for _ in range(n)]

        return self.func(n - 1, 3, matrix, dp)


s = Solution()

k1 = s.ninjaTraining(
    [
        [10, 40, 70],
        [20, 50, 80],
        [30, 60, 90],
    ]
)

k2 = s.ninjaTraining(
    [
        [70, 40, 10],
        [180, 20, 5],
        [200, 60, 30],
    ]
)

print(k1)
print(k2)
