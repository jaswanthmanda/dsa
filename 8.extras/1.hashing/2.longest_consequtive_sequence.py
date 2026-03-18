# Longest consequtive sequence
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hash values
        hash_values = set(nums)

        # counter
        counter = 0

        for item in hash_values:
            if item - 1 not in hash_values:
                temp_item = item
                temp_count = 1
                while temp_item + 1 in hash_values:
                    temp_item += 1
                    temp_count += 1

                counter = max(counter, temp_count)

        return counter


s = Solution()

k1 = s.longestConsecutive([100, 4, 200, 1, 3, 2])

k2 = s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])

k3 = s.longestConsecutive([1, 0, 1, 2])

print(k1)
print(k2)
print(k3)
