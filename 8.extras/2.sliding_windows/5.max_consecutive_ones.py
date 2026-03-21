# Max consecutive ones
"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

"""


class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        j = 0
        count_ones = 0
        ans = 0

        while j < len(nums):
            if nums[j] == 1:
                count_ones += 1

            while (j - i + 1) - count_ones > k:
                if nums[i] == 1:
                    count_ones -= 1
                i += 1

            ans = max(ans, (j - i + 1))
            j += 1

        return ans
