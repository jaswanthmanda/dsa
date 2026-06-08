# Is Subsequence


# Recursion
class Solution:
    def f(self, i, j, s, t):
        if i < 0:
            if j > 0:
                return False
            return True

        if j < 0:
            return True

        # take
        if s[i] == t[j]:
            return self.f(i - 1, j - 1, s, t)

        return self.f(i - 1, j, s, t)

    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m > n:
            return False

        return self.f(m - 1, n - 1, t, s)


# Memoization
class SolutionMemoization:
    def f(self, i, j, s, t, dp):
        if j < 0:
            return True

        if i < 0:
            return False

        if dp[i][j] is not None:
            return dp[i][j]

        # take
        if s[i] == t[j]:
            dp[i][j] = self.f(i - 1, j - 1, s, t, dp)

            return dp[i][j]

        # not take
        dp[i][j] = self.f(i - 1, j, s, t, dp)

        return dp[i][j]

    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        dp = [[None] * m for _ in range(n)]

        if m > n:
            return False

        return self.f(n - 1, m - 1, t, s, dp)


class SolutionTabulation:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        dp = [[False] * (n + 1) for i in range(m + 1)]

        for i in range(n + 1):
            dp[0][i] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[m][n]


class SolutionTwoPointerOptimized:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
