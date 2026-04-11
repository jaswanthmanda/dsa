# Max Subarray
from typing import List

# kadane's algo


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n
        n = len(nums)

        # base case
        if n in [0, 1]:
            return sum(nums)

        # max tracker
        maxTracker = max(nums)
        summer = 0
        for item in nums:
            summer += item

            maxTracker = max(maxTracker, summer)

            if summer < 0:
                summer = 0

        return maxTracker
