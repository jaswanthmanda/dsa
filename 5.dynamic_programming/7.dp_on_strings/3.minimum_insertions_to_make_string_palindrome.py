# Minimum insertions to make string palindrome
"""
Given a string s, find the minimum number of insertions needed to make it a palindrome.
A palindrome is a sequence that reads the same backward as forward.
You can insert characters at any position in the string.
"""
"""
Example 1:
Input: s = "abcaa"
Output: 2
Explanation: Insert 2 characters "c", and "b" to make "abcacba", which is a palindrome.

Example 2:
Input: s = "ba"
Output: 1
Explanation: Insert "a" at the beginning to make "aba", which is a palindrome.
"""
"""
Constraints
- 1 <= s.length <= 1000,
- s consists of only lowercase English letters
"""


class Solution:
    def f(self, i, j, s1, s2, dp):
        if i == 0 or j == 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i - 1] == s2[j - 1]:
            return 1 + self.f(i - 1, j - 1, s1, s2, dp)

        dp[i][j] = max(
            self.f(i - 1, j, s1, s2, dp),
            self.f(i, j - 1, s1, s2, dp),
        )

        return dp[i][j]

    def minInsertion(self, s):
        m = len(s)
        n = len(s)

        s1 = s
        kk = list(s)
        kk.reverse()
        s2 = "".join(kk)

        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        return m - self.f(m, n, s1, s2, dp)


class SolutionOptimal:
    def minInsertion(self, s):
        m = len(s)
        n = len(s)

        s1 = s
        kk = list(s)
        kk.reverse()
        s2 = "".join(kk)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            dp[i][0] = 0

        for j in range(n):
            dp[0][j] = 0

        max_ans = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1],
                    )

                max_ans = max(max_ans, dp[i][j])

        return m - max_ans


class SolutionOptimalSpace:
    def minInsertion(self, s):
        m = len(s)
        n = len(s)

        s1 = s
        kk = list(s)
        kk.reverse()
        s2 = "".join(kk)

        prev, curr = [0] * (n + 1), [0] * (m + 1)

        for i in range(m):
            prev[i] = 0

        max_ans = 0

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(
                        prev[j],
                        curr[j - 1],
                    )

                max_ans = max(max_ans, curr[j])

            prev = curr

        return m - max_ans


s = SolutionOptimalSpace()

k1 = s.minInsertion("abcaa")

k2 = s.minInsertion("ba")

print(k1)
print(k2)
