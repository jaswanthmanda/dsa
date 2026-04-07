# Two sum


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use a hashmap
        mp = {}

        for i, item in enumerate(nums):
            rem = target - item
            if rem in mp:
                return [mp[rem], i]

            mp[item] = i

        return []
