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
        pass

    def editDistance(self, start, target):
        pass


s = Solution()

k1 = s.editDistance("planet", "plan")

k2 = s.editDistance("abcdefg", "azced")

print(k1)
print(k2)
