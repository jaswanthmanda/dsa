# Longest Repeating Character Replacement
from collections import defaultdict


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        # base case
        if n in [0, 1]:
            return n

        freq = defaultdict(int)

        i = 0
        j = 0
        max_freq = 0
        ans = 0
        while i < n and j < n:
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_freq = max(max_freq, freq[s[j]])

            if (j - i + 1) - max_freq <= k:
                ans = max(ans, (j - i + 1))
            else:
                freq[s[i]] -= 1
                i += 1

            j += 1

        return ans
