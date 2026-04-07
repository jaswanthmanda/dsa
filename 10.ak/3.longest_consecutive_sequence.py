# Longest consequtive sequence


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hash map
        hash_values = set(nums)

        temp_count = 0
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
