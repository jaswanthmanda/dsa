# Max subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n
        n = len(nums)

        # base case
        if n in [0, 1]:
            return sum(nums)

        maxTracker = max(nums)
        summer = 0
        for item in nums:
            summer += item
            maxTracker = max(maxTracker, summer)

            if summer < 0:
                summer = 0

        return maxTracker
