# Distinct Subsequences
"""
Given two strings s and t, return the number of distinct subsequences of s that equal t.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde" while "aec" is not.

The task is to count how many different ways we can form t from
s by deleting some (or no) characters from s.
Return the result modulo 109+7.
"""
"""
Example 1:
Input: s = "axbxax", t = "axa"
Output: 2
Explanation: In the string "axbxax", there are two distinct subsequences "axa":

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation: In the string "babgbag", there are five distinct subsequences "bag":
(ba)(b)(ga)(g)
(ba)(bg)(ag)
(bab)(ga)(g)
(bab)(g)(ag)
(babg)(a)(g)
"""
"""
Constraints:
- 1 <= s.length, t.length <= 1000
"""


class Solution:
    def f(self, i, j, s1, s2, dp):
        if j == 0:
            return 1

        if i == 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = self.f(
                i - 1,
                j,
                s1,
                s2,
                dp,
            ) + self.f(
                i - 1,
                j - 1,
                s1,
                s2,
                dp,
            )
        else:
            dp[i][j] = self.f(i - 1, j, s1, s2, dp)

        return dp[i][j]

    def distinctSubsequences(self, s, t):
        MOD = (10**9) + 7
        m = len(s)
        n = len(t)

        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        return self.f(m, n, s, t, dp) % MOD


class SolutionOptimal:
    def distinctSubsequences(self, s, t):
        MOD = (10**9) + 7
        m = len(s)
        n = len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            dp[i][0] = 1

        for j in range(1, n):
            dp[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n] % MOD


class SolutionOptimalSpace:
    def distinctSubsequences(self, s, t):
        MOD = (10**9) + 7

        m = len(s)
        n = len(t)

        prev, curr = [0] * (n + 1), [0] * (n + 1)

        prev[0] = curr[0] = 1

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            curr[0] = 1
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j] + prev[j - 1]
                else:
                    curr[j] = prev[j]

            prev = curr

        return prev[n] % MOD


class SolutionOptimal1DSpace:
    def distinctSubsequences(self, s, t):
        MOD = (10**9) + 7

        m = len(s)
        n = len(t)

        prev = [0] * (n + 1)

        prev[0] = 1

        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    prev[j] = prev[j] + prev[j - 1]

        return prev[n] % MOD


s = SolutionOptimal1DSpace()

k1 = s.distinctSubsequences("axbxax", "axa")

k2 = s.distinctSubsequences("babgbag", "bag")

print(k1)
print(k2)
