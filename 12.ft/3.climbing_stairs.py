# Climbing stairs


# Recursive
class Solution:
    def climbStairs(self, n: int) -> int:
        # either 1 step or 2 step (implies fibonacci series)
        if n in [0, 1]:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


#  Memoization
class SolutionMemoization:
    def climbStairs(self, n: int) -> int:
        # memo
        memo = {}

        return self.helper(n, memo)

    def helper(self, n: int, memo: dict) -> int:
        if n in [0, 1]:
            return 1

        if n not in memo:
            memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)

        return memo[n]


# Tabulation
class SolutionTabulation:
    def climbStairs(self, n: int) -> int:
        if n in [0, 1]:
            return 1

        dp = [0] * (n + 1)

        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# Tabulation Space Optimization
class SolutionTabulationSpaceOptimization:
    def climbStairs(self, n: int) -> int:
        if n in [0, 1]:
            return 1

        prev = 1
        curr = 1

        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp

        return curr
