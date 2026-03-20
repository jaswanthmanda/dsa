# Minimum window substring
from collections import defaultdict


class Solution(object):
    def minWindowBrute(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # n
        n = len(s)
        m = len(t)

        min_len = float("inf")
        sIndex = -1
        for i in range(n):
            freq = {}
            cnt = 0
            for j in range(m):
                freq[t[j]] = freq.get(t[j], 0) + 1

            for j in range(i, n):
                if s[j] in freq and freq[s[j]] > 0:
                    cnt += 1
                    freq[s[j]] = freq[s[j]] - 1
                if cnt == m:
                    min_len = min(min_len, (j - i + 1))
                    sIndex = i
                    break

        if sIndex == -1:
            return ""

        return "".join(list(s)[sIndex : sIndex + min_len])

    def minWindowOptimal(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # n
        n = len(s)
        m = len(t)

        freq = defaultdict(int)

        for i in range(m):
            freq[t[i]] += 1

        i = 0
        j = 0
        minLen = float("inf")
        sIndex = -1
        cnt = 0
        while j < n:
            if freq[s[j]] > 0:
                cnt += 1
            freq[s[j]] -= 1
            while cnt == m:
                if (j - i + 1) < minLen:
                    minLen = min(minLen, (j - i + 1))
                    sIndex = i

                freq[s[i]] += 1
                if freq[s[i]] > 0:
                    cnt -= 1

                i += 1

            j += 1

        return "" if sIndex == -1 else "".join(list(s)[sIndex : sIndex + minLen])
