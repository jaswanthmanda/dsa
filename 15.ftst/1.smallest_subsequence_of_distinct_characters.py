# Smallest subsequence of distinct characters

"""
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.


Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

Constraints:

- 1 <= s.length <= 1000
- s consists of lowercase English letters.
"""


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # base logic
        mapp = set()
        stack = []
        last = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c in mapp:
                continue

            while (
                stack != []
                and stack[-1] > c
                and last[stack[-1]] > i
            ):
                mapp.remove(stack.pop())

            stack.append(c)
            mapp.add(c)

        return "".join(stack)
