# Longest string chain
"""
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly
one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2,
word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.
"""
"""
Example 1:
Input: words = ["a", "ab", "abc", "abcd", "abcde"]
Output: 5
Explanation: The longest chain is ["a", "ab", "abc", "abcd", "abcde"].


Example 2:
Input: words = ["dog", "dogs", "dots", "dot", "d", "do"]
Output: 4
Explanation: The longest chain is ["d", "do", "dot", "dots"].
Each word is formed by inserting one character into the previous word.
"""
"""
Constraints
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 20
- words[i] only consists of lowercase English letters.
"""


class Solution:
    def longestStringChain(self, words):
        n = len(words)
        words.sort()

        parent = [0] * n
        dp = [1] * n

        maxLen = 0
        # lastIndex = 0

        for i in range(n):
            parent[i] = i
            for prevInd in range(i):
                kemp1 = set(words[i])
                kemp2 = set(words[prevInd])
                # print(words[i], words[prevInd], kemp1.difference(kemp2))

                kemp1.intersection_update(kemp2)

                if sorted(list(kemp1)) == sorted(list(kemp2)):
                    if dp[i] < dp[prevInd] + 1:
                        dp[i] = dp[prevInd] + 1
                        parent[i] = prevInd
                    elif dp[i] == dp[prevInd] + 1 and prevInd < parent[i]:
                        parent[i] = prevInd

            if maxLen < dp[i]:
                maxLen = dp[i]
                # lastIndex = i

        # print(dp)
        return maxLen


s = Solution()

k1 = s.longestStringChain(["a", "ab", "abc", "abcd", "abcde"])

k2 = s.longestStringChain(["dog", "dogs", "dots", "dot", "d", "do"])

print(k1)
print(k2)
