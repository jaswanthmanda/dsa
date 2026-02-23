# Wildcard matching
"""
Given a string str and a pattern pat, implement a pattern matching function that supports the following special characters:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The pattern must match the entire string.
"""
"""
Example 1:
Input: str = "xaylmz", pat = "x?y*z"
Output: true
Explanation:
The pattern "x?y*z" matches the string "xaylmz":
- '?' matches 'a'
- '*' matches "lm"
- 'z' matches 'z'


Example 2:
Input: str = "xyza", pat = "x*z"
Output: false
Explanation:
The pattern "x*z" does not match the string "xyza" because
there is an extra 'a' at the end of the string that is not matched by the pattern.
"""
"""
Constraints:
- 0 <= length of(str, pattern) <= 200
"""


class Solution:
    def f(self, i, j, patt, strr, dp):
        if i == 0 and j == 0:
            return True
        if i == 0 and j > 0:
            return False
        if j == 0 and i > 0:
            for ii in range(1, i + 1):
                if patt[ii - 1] != "*":
                    return False
            return True

        if dp[i][j] != -1:
            return dp[i][j]

        if patt[i - 1] == strr[j - 1] or patt[i - 1] == "?":
            dp[i][j] = self.f(i - 1, j - 1, patt, strr, dp)
            return dp[i][j]
        if patt[i - 1] == "*":
            dp[i][j] = self.f(i - 1, j, patt, strr, dp) or self.f(
                i,
                j - 1,
                patt,
                strr,
                dp,
            )
            return dp[i][j]

        dp[i][j] = False

        return False

    def wildCard(self, str: str, pat: str) -> bool:
        m = len(pat)
        n = len(str)

        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        return self.f(m, n, pat, str, dp)


class SolutionOptimal:
    def wildCard(self, str: str, pat: str) -> bool:
        m = len(pat)
        n = len(str)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True
        for j in range(n):
            dp[0][j] = False

        for i in range(m):
            flag = True
            for ii in range(1, i + 1):
                if pat[ii - 1] != "*":
                    flag = False
                    break

            dp[i][0] = flag

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pat[i - 1] == str[j - 1] or pat[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif pat[i - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False

        return dp[m][n]


class SolutionOptimalSpace1d:
    def wildCard(self, str: str, pat: str) -> bool:
        m = len(pat)
        n = len(str)

        prev, curr = [False] * (n + 1), [False] * (n + 1)

        prev[0] = True
        for j in range(1, n + 1):
            prev[j] = False

        for i in range(1, m + 1):
            curr = [False] * (n + 1)

            flag = True
            for ii in range(1, i + 1):
                if pat[ii - 1] != "*":
                    flag = False
                    break

            curr[0] = flag

            for j in range(1, n + 1):
                if pat[i - 1] == str[j - 1] or pat[i - 1] == "?":
                    curr[j] = prev[j - 1]
                elif pat[i - 1] == "*":
                    curr[j] = prev[j] or curr[j - 1]
                else:
                    curr[j] = False

            prev = curr

        return prev[n]


s = SolutionOptimalSpace1d()

k1 = s.wildCard("xaylmz", "x?y*z")

k2 = s.wildCard("xyza", "x*z")

print(k1)
print(k2)
