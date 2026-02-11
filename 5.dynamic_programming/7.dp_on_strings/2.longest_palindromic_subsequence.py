# Longest Palindromic Subsequence
"""
Given a string, Find the longest palindromic subsequence length in given string.

A palindrome is a sequence that reads the same backwards as forward.

A subsequence is a sequence that can be derived from another
sequence by deleting some or no elements without changing the order of the remaining elements.
"""
"""
Example 1:
Input: s = "eeeme"
Output: 4
Explanation: The longest palindromic subsequence is "eeee", which has a length of 4.


Example 2:
Input: s = "annb"
Output: 2
Explanation: The longest palindromic subsequence is "nn", which has a length of 2.
"""
"""
Constraints
- 1 ≤ s.length ≤ 1000
"""


class Solution:
    def f(self, i, j, s1, s2, dp):
        if i == 0 or j == len(s2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i - 1] == s2[j]:
            return 1 + self.f(i - 1, j + 1, s1, s2, dp)

        dp[i][j] = max(
            self.f(i - 1, j, s1, s2, dp),
            self.f(i, j + 1, s1, s2, dp),
        )

        return dp[i][j]

    def longestPalinSubseq(self, s):
        m = len(s)
        # n = len(s)
        dp = [[-1] * (m + 1) for _ in range(m + 1)]

        return self.f(m, 0, s, s, dp)


class SolutionOptimal:
    def longestPalinSubseq(self, s):
        m = len(s)
        n = len(s)

        s1 = s
        s2 = s

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(m):
            dp[i][0] = 0

        for j in range(n):
            dp[n - 1][j] = 0

        ans = 0

        for i in range(1, m + 1):
            for j in range(n - 1, -1, -1):
                if s1[i - 1] == s2[j]:
                    dp[i][j] = 1 + dp[i - 1][j + 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j + 1],
                    )

                ans = max(ans, dp[i][j])

        return ans


class SolutionOptimalSpace:
    def longestPalinSubseq(self, s):
        m = len(s)
        n = len(s)

        s1 = s
        s2 = s

        prev, curr = [0] * (m + 1), [0] * (n + 1)

        for i in range(m):
            prev[i] = 0

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if s1[i - 1] == s2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(
                        prev[j],
                        curr[j + 1],
                    )

            prev = curr

        return max(prev)


s = SolutionOptimalSpace()

k1 = s.longestPalinSubseq("eeeme")

k2 = s.longestPalinSubseq("annb")

print(k1)
print(k2)
