# Permutations


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            x = nums[i]

            remaining = nums[:i] + nums[i + 1 :]

            perms = self.permute(remaining)

            for p in perms:
                res.append([x] + p)

        return res
