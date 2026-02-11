# Minimum insertions or deletions to convert A to B
"""
Given two strings str1 and str2, find the minimum number of insertions and deletions in string str1 required to transform str1 into str2.

Insertion and deletion of characters can take place at any position in the string.
"""
"""
Example 1:
Input: str1 = "kitten", str2 = "sitting"
Output: 5
Explanation: To transform "kitten" to "sitting", delete "k" and insert "s" to get "sitten",
then insert "i" to get "sittin", and insert "g" at the end to get "sitting".


Example 2:
Input: str1 = "flaw", str2 = "lawn"
Output: 2
Explanation: To transform "flaw" to "lawn", delete "f" and insert "n" at the end. Hence minimum number of operations required is 2".
"""
"""
Constraints:
- 1 ≤ str1.length, str2.length ≤ 1000
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

    def minOperations(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        ans = self.f(m, n, str1, str2, dp)

        return (m - ans) + (n - ans)


class SolutionOptimal:
    def minOperations(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            dp[i][0] = 0

        for j in range(n):
            dp[0][j] = 0

        ans = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                ans = max(ans, dp[i][j])

        return (m - ans) + (n - ans)


class SolutionOptimalSpace:
    def minOperations(self, str1, str2):
        m = len(str1)
        n = len(str2)

        prev, curr = [0] * (n + 1), [0] * (n + 1)

        for j in range(n):
            prev[j] = 0

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])

            prev = curr

        ans = max(prev)

        return (m - ans) + (n - ans)


s = SolutionOptimalSpace()

k1 = s.minOperations("kitten", "sitting")

k2 = s.minOperations("flaw", "lawn")

print(k1)
print(k2)
