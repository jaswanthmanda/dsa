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
    def check_for_all(self, word1, word2):
        if len(word2) != len(word1) + 1:
            return False

        i = 0
        j = 0
        skipped = False
        while i < len(word1) and j < len(word2):
            if word1[i] == word2[j]:
                i += 1
                j += 1
            else:
                if skipped:
                    return False
                skipped = True
                j += 1

        return True

    def longestStringChain(self, words):
        n = len(words)
        words.sort(key=len)

        dp = [1] * n

        maxLen = 1

        for i in range(n):
            for prevInd in range(i):
                if self.check_for_all(words[prevInd], words[i]):
                    dp[i] = max(dp[i], dp[prevInd] + 1)

            maxLen = max(maxLen, dp[i])

        return maxLen


s = Solution()

k1 = s.longestStringChain(["a", "ab", "abc", "abcd", "abcde"])

k2 = s.longestStringChain(["dog", "dogs", "dots", "dot", "d", "do"])

print(k1)
print(k2)
