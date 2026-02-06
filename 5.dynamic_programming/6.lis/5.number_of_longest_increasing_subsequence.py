# Number of longest increasing subsequence
"""
Given an integer array nums, find the number of Longest Increasing Subsequences (LIS) in the array.
"""
"""
Example 1:
Input: nums = [1, 3, 5, 4, 7]
Output: 2
Explanation: There are two LIS of length 4:
[1, 3, 4, 7]
[1, 3, 5, 7].


Example 2:
Input: nums = [2, 2, 2, 2, 2]
Output: 5
Explanation: All elements are the same, so every single element can form an LIS of length 1.
There are 5 such subsequences.
"""
"""
Constraints
- 1 <= nums.length <= 103
- -106 <= nums[i] <= 106
"""


class Solution:
    def numberOfLIS(self, nums):
        n = len(nums)

        dp = [1] * n
        counter = [1] * n

        maxLen = 0
        ans = 0

        for i in range(n):
            for prevInd in range(i):
                if nums[i] > nums[prevInd]:
                    if dp[i] < dp[prevInd] + 1:
                        dp[i] = dp[prevInd] + 1
                        counter[i] = counter[prevInd]
                    elif dp[i] == dp[prevInd] + 1:
                        counter[i] += counter[prevInd]

            if maxLen < dp[i]:
                maxLen = dp[i]

        ans = 0

        for i in range(n):
            if dp[i] == maxLen:
                ans += counter[i]

        return ans


s = Solution()

k1 = s.numberOfLIS([1, 3, 5, 4, 7])

k2 = s.numberOfLIS([2, 2, 2, 2, 2])

print(k1)
print(k2)
