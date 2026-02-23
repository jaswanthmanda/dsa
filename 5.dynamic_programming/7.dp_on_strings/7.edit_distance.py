# Edit Distance
"""
Given two strings start and target, you need to determine the minimum number of operations
required to convert the string start into the string target.
The operations you can use are:

Insert a character: Add any single character at any position in the string.

Delete a character: Remove any single character from the string.

Replace a character: Change any single character in the string to another character.

The goal is to transform start into target using the fewest number of these operations.
"""
"""
Example 1:
Input: start = "planet", target = "plan"
Output: 2
Explanation:
To transform "planet" into "plan", the following operations are required:
1. Delete the character 'e': "planet" -> "plan"
2. Delete the character 't': "plan" -> "plan"
Thus, a total of 2 operations are needed.


Example 2:
Input: start = "abcdefg", target = "azced"
Output: 4
Explanation:
To transform "abcdefg" into "azced", the following operations are required:
1. Replace 'b' with 'z': "abcdefg" -> "azcdefg"
2. Delete 'd': "azcdefg" -> "azcefg"
3. Delete 'f': "azcefg" -> "azceg"
4. Replace 'g' with 'd': "azceg" -> "azced"
Thus, a total of 4 operations are needed.
"""
"""
Constraints:
- 1 ≤ start.length, target.length ≤ 1000
"""


class Solution:
    def f(self, i, j, s1, s2, dp):
        if i == 0:
            return j
        if j == 0:
            return i

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i - 1] == s2[j - 1]:
            return 0 + self.f(i - 1, j - 1, s1, s2, dp)

        dp[i][j] = 1 + min(
            self.f(i - 1, j, s1, s2, dp),
            min(
                self.f(i, j - 1, s1, s2, dp),
                self.f(i - 1, j - 1, s1, s2, dp),
            ),
        )

        return dp[i][j]

    def editDistance(self, start, target):
        m = len(start)
        n = len(target)

        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        return self.f(m, n, start, target, dp)


class SolutionOptimalSpace:
    def editDistance(self, start, target):
        m = len(start)
        n = len(target)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if start[i - 1] == target[j - 1]:
                    dp[i][j] = 0 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        min(dp[i][j - 1], dp[i - 1][j - 1]),
                    )

        return dp[m][n]


class SolutionOptimalSpace1d:
    def editDistance(self, start, target):
        m = len(start)
        n = len(target)

        prev, curr = [0] * (n + 1), [0] * (n + 1)

        for j in range(n + 1):
            prev[j] = j

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            curr[0] = i
            for j in range(1, n + 1):
                if start[i - 1] == target[j - 1]:
                    curr[j] = 0 + prev[j - 1]
                else:
                    curr[j] = 1 + min(
                        prev[j],
                        min(curr[j - 1], prev[j - 1]),
                    )

            prev = curr

        return prev[n]


s = SolutionOptimalSpace1d()

k1 = s.editDistance("planet", "plan")

k2 = s.editDistance("abcdefg", "azced")

print(k1)
print(k2)
