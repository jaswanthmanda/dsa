# Longest substring without repeating characters


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        if n == 0 or n == 1:
            return 0

        hash_set = set()

        i = 0
        j = 1
        ans = 1
        hash_set.add(s[0])
        while i < n and j < n:
            if s[j] not in hash_set:
                hash_set.add(s[j])
                ans = max(ans, len(hash_set))
                j += 1
            elif s[j] in hash_set:
                hash_set.remove(s[i])
                i += 1

        ans = max(ans, len(hash_set))

        return ans


s = Solution()

k1 = s.lengthOfLongestSubstring("abcabcbb")

k2 = s.lengthOfLongestSubstring("bbbbb")

k3 = s.lengthOfLongestSubstring("pwwkew")

print(k1)
print(k2)
print(k3)
