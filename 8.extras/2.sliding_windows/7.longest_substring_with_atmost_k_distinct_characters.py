# Longest substring with atmost k distinct characters


class Solution:
    def kDistinctChar(self, s, k):
        # your code goes here
        n = len(s)

        # base case
        if n in [0, 1]:
            return n

        hash_map = {}
        i = 0
        j = 1
        ans = 0
        hash_map[s[i]] = 1
        while j < n:
            hash_map[s[j]] = hash_map.get(s[j], 0) + 1

            while len(hash_map) > k:
                if hash_map[s[i]] - 1 > 0:
                    hash_map[s[i]] -= 1
                else:
                    del hash_map[s[i]]
                i += 1

            ans = max(ans, (j - i + 1))
            j += 1

        return ans
