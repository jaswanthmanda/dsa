# Shortest common supersequence
"""
Given two strings str1 and str2, find the shortest common supersequence.

The shortest common supersequence is the shortest string that contains both str1 and str2 as subsequences.
"""
"""
Example 1:
Input: str1 = "mno", str2 = "nop"
Output: "mnop"
Explanation: The shortest common supersequence is "mnop".
It contains "mno" as the first three characters and "nop" as the last three characters, thus including both strings as subsequences.

Example 2:
Input: str1 = "dynamic", str2 = "program"
Output: "dynprogramic"
Explanation: The shortest common supersequence is "dynprogramic". It includes all characters from both "dynamic" and "program", with minimal overlap.
For example, "dynamic" appears as "dyn...amic" and "program" appears as "...program..." within "dynprogramic".
"""
"""
Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of lowercase English letters.
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            dp[i][0] = 0

        for j in range(n):
            dp[0][j] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        ans = ""
        i = m
        j = n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                ans += str1[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                ans += str1[i - 1]
                i -= 1
            else:
                ans += str2[j - 1]
                j -= 1

        while i > 0:
            ans += str1[i - 1]
            i -= 1

        while j > 0:
            ans += str2[j - 1]
            j -= 1

        kk = list(ans)
        kk.reverse()
        new_ans = "".join(kk)

        return new_ans


s = Solution()

k1 = s.shortestCommonSupersequence("mno", "nop")

k2 = s.shortestCommonSupersequence("dynamic", "program")

print(k1)
print(k2)
