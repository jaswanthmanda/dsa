# Longest Common Subsequence


class Solution:
    def f(self, ind1, ind2, text1, text2):
        # return ind
        if ind1 < 0 or ind2 < 0:
            return 0

        # return ind
        if text1[ind1] == text2[ind2]:
            return 1 + self.f(ind1 - 1, ind2 - 1, text1, text2)

        # return max
        return max(
            self.f(ind1 - 1, ind2, text1, text2),
            self.f(ind1, ind2 - 1, text1, text2),
        )

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.f(len(text1) - 1, len(text2) - 1, text1, text2)


class SolutionOptimal:
    def f(self, ind1, ind2, text1, text2, dp):
        # return ind
        if ind1 < 0 or ind2 < 0:
            return 0

        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        # return ind
        if text1[ind1] == text2[ind2]:
            dp[ind1][ind2] = 1 + self.f(ind1 - 1, ind2 - 1, text1, text2)
            return dp[ind1][ind2]

        # return max
        dp[ind1][ind2] = max(
            self.f(ind1 - 1, ind2, text1, text2, dp),
            self.f(ind1, ind2 - 1, text1, text2, dp),
        )

        return dp[ind1][ind2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.f(len(text1) - 1, len(text2) - 1, text1, text2, dp)


class SolutionOptimalSpace:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for ind1 in range(1, m + 1):
            for ind2 in range(1, n + 1):
                if text1[ind1] == text2[ind2]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        return dp[m][n]


class SolutionOptimalSpace1D:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        curr = [0] * n + 1
        prev = [0] * n + 1

        for ind1 in range(1, m + 1):
            curr = [0] * (n + 1)
            for ind2 in range(1, n + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    curr[ind2] = 1 + prev[ind2 - 1]
                else:
                    curr[ind2] = max(prev[ind2], curr[ind2 - 1])

            prev = curr

        return curr[n]
