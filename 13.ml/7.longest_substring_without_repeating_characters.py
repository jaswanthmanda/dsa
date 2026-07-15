# Longest substring without repeating characters

"""Given a string s, find the length of the longest substring without duplicate characters.

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

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n
        n = len(s)

        if n in [0, 1]:
            return n

        # main logic
        i = 0
        j = 1
        sett = set([s[0]])

        max_trc = 1
        while i < n and j < n:

            while i < n and s[j] in sett:
                sett.remove(s[i])
                i += 1

            sett.add(s[j])

            max_trc = max(max_trc, j - i + 1)
            j += 1

        return max_trc


"""
TC: O(n)
SC: O(n)
"""
