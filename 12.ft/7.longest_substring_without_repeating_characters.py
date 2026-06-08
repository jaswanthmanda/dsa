# Longest substring without repeating characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n
        n = len(s)

        if n in [0, 1]:
            return n

        i = 0
        j = 1
        mp = set([s[i]])
        max_len = 0

        while j < n:
            if s[j] not in mp:
                mp.add(s[j])
                j += 1
            else:
                mp.remove(s[i])
                i += 1
            max_len = max(max_len, len(mp))

        return max_len
