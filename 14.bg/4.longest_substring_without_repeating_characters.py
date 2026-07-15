# Longest substring without repeating characters

"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n in [0, 1]:
            return n

        k = set()

        l = 0
        k.add(s[0])
        r = 1
        ans = float("-inf")
        while l < n and r < n:
            if s[r] in k:
                k.remove(s[l])
                l += 1
            else:
                k.add(s[r])
                r += 1

            ans = max(ans, r - l + 1)

        return ans
