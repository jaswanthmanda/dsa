# Longest common substring
"""
Given two strings str1 and str2, find the length of their longest common substring.

A substring is a contiguous sequence of characters within a string.
"""
"""
Example 1:
Input: str1 = "abcde", str2 = "abfce"
Output: 2
Explanation: The longest common substring is "ab", which has a length of 2.

Example 2:
Input: str1 = "abcdxyz", str2 = "xyzabcd"
Output: 4
Explanation: The longest common substring is "abcd", which has a length of 4.
"""
"""
Constraints
- n=str1.length
- m=str2.length
- 1<= n, m <=103
- str1 and str2 are in lowercase alphabet
"""


class SolutionOptimal:
    def longestCommonSubstr(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(m + 1):
            dp[j][0] = 0

        for i in range(n + 1):
            dp[0][i] = 0

        ans = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0

        return ans


class SolutionOptimalSpace:
    def longestCommonSubstr(self, str1, str2):
        m = len(str1)
        n = len(str2)

        prev, curr = [0] * (n + 1), [0] * (n + 1)

        for j in range(m + 1):
            prev[0] = 0

        ans = 0

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                    ans = max(ans, curr[j])
                else:
                    curr[j] = 0

            prev = curr

        return ans


s = SolutionOptimalSpace()

k1 = s.longestCommonSubstr("abcde", "abfce")

k2 = s.longestCommonSubstr("abcdxyz", "xyzabcd")

print(k1)
print(k2)
