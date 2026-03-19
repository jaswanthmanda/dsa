# Longest subarray with sum K


class Solution(object):
    def longestSubarrayWithSumK(self, nums, k):
        # n
        n = len(nums)

        prefixMap = {}

        maxLen = 0
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]
            if curr_sum == k:
                maxLen = max(maxLen, i + 1)

            rem = maxLen - k
            if rem in prefixMap:
                maxLen = max(maxLen, i - prefixMap[rem] + 1)

            if curr_sum not in prefixMap:
                prefixMap[curr_sum] = i

        return maxLen
