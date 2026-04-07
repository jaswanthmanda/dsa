# Longest substring without repeating chars


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # base case
        if n in [0, 1]:
            return s

        store = set()

        i = 0
        j = 1
        store.add(s[i])
        max_len = 0
        while j < n:
            if s[j] not in store:
                max_len = max((j - i + 1), max_len)
                store.add(s[j])
                j += 1
            else:
                store.remove(s[i])
                i += 1

        max_len = max(max_len, len(store))

        return max_len
