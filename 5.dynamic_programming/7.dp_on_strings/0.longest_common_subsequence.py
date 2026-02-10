# Longest common subsequence
"""
Given two strings str1 and str2, find the length of their longest common subsequence.

A subsequence is a sequence that appears in the same relative order but not necessarily
contiguous and a common subsequence of two strings is a subsequence that is common to both strings.
"""
"""
Example 1:
Input: str1 = "bdefg", str2 = "bfg"
Output: 3
Explanation: The longest common subsequence is "bfg", which has a length of 3.

Example 2:
Input: str1 = "mnop", str2 = "mnq"
Output: 2
Explanation: The longest common subsequence is "mn", which has a length of 2.
"""
"""
Constraints
- n=str1.length
- m=str2.length
- 1<= n, m <=103
- str1 and str2 are in lowercase alphabet
"""


class Solution:
    def f(self, i, j, str1, trgt1, dp):
        if i == 0 or j == 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if str1[i - 1] == trgt1[j - 1]:
            return 1 + self.f(i - 1, j - 1, str1, trgt1, dp)

        dp[i][j] = max(
            self.f(i - 1, j, str1, trgt1, dp),
            self.f(i, j - 1, str1, trgt1, dp),
        )

        return dp[i][j]

    def lcs(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        return self.f(m, n, str1, str2, dp)


class SolutionOptimal:
    def lcs(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(m + 1):
            dp[j][0] = 0

        for i in range(n + 1):
            dp[0][i] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


class SolutionOptimalSpace:
    def lcs(self, str1, str2):
        m = len(str1)
        n = len(str2)

        prev, curr = [0] * (n + 1), [0] * (n + 1)

        for i in range(n + 1):
            prev[i] = 0

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])

            prev = curr

        return prev[n]


s = SolutionOptimal()


k1 = s.lcs("bdefg", "bfg")

k2 = s.lcs("mnop", "mnq")

print(k1)
print(k2)
