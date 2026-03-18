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
        freq = defaultdict(int)
        i = 0
        max_freq = 0
        ans = 0

        for j in range(n):
            freq[s[j]] += 1
            max_freq = max(max_freq, freq[s[j]])

            while (j - i + 1) - max_freq > k:
                freq[s[i]] -= 1
                i += 1

            ans = max(ans, j - i + 1)

        return ans
