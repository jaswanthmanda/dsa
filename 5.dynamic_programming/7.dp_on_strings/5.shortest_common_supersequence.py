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
    def f(self, i, j, s1, s2):
        if i == 0 or j == 0:
            return 0

        if s1[i - 1] == s2[j - 1]:
            self.stack.append(s1[i - 1])
            return self.f(i - 1, j - 1, s1, s2)

        return self.f(i - 1, j, s1, s2) + self.f(i, j - 1, s1, s2)

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        self.stack = []

        self.f(m, n, str1, str2)
        print(self.stack)

        ans = ""

        i = 0
        j = 0
        while i < m or j < n:
            if i < m:
                if len(self.stack) > 0:
                    if self.stack[-1] != str1[i]:
                        ans += str1[i]
                        i += 1
                    else:
                        if j < n:
                            if len(self.stack) > 0:
                                if self.stack[-1] != str2[j]:
                                    ans += str2[j]
                                    j += 1
                                else:
                                    ans += self.stack.pop()
                                    i += 1
                                    j += 1

        return ans


s = Solution()

k1 = s.shortestCommonSupersequence("mno", "nop")

k2 = s.shortestCommonSupersequence("dynamic", "program")

print(k1)
print(k2)
