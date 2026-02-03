import bisect

# Longest increasing subsequence
"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3, 6, 2, 7] is a subsequence of [0, 3, 1, 6, 2, 2, 7].

The task is to find the length of the longest subsequence in which every element is greater than the previous one.
"""
"""
Example 1:
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], and its length is 4.

Example 2:
Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4
Explanation: The longest increasing subsequence is [0, 1, 2, 3], and its length is 4
"""
"""
Constraints:
- 1 <= nums.length <= 10^5
- -10^6 <= nums[i] <= 10^6
"""


class Solution:
    def f(self, ind, prev_ind, arr, n, dp):
        if ind == n:
            return 0

        if dp[ind][prev_ind + 1] != -1:
            return dp[ind][prev_ind + 1]

        # not take
        lenn = 0 + self.f(ind + 1, prev_ind, arr, n, dp)
        if prev_ind == -1 or (arr[ind] > arr[prev_ind]):
            # take
            lenn = max(lenn, 1 + self.f(ind + 1, ind, arr, n, dp))

        dp[ind][prev_ind + 1] = lenn

        return lenn

    def LIS(self, nums):
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]
        return self.f(0, -1, nums, n, dp)


class SolutionOptimal:
    def LIS(self, nums):
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):
            for prev_ind in range(ind - 1, -2, -1):
                # Not Take case
                # not take
                lenn = 0 + dp[ind + 1][prev_ind + 1]
                if prev_ind == -1 or (nums[ind] > nums[prev_ind]):
                    # take
                    lenn = max(lenn, 1 + dp[ind + 1][ind + 1])

                dp[ind][prev_ind + 1] = lenn

        return dp[0][0]


class SolutionOptimalSpace2D:
    def LIS(self, nums):
        n = len(nums)
        # dp = [[0] * (n + 1) for _ in range(n + 1)]
        prev, curr = [0] * (n + 1), [0] * (n + 1)

        for ind in range(n - 1, -1, -1):
            curr = [0] * (n + 1)
            for prev_ind in range(ind - 1, -2, -1):
                # Not Take case
                # not take
                lenn = 0 + prev[prev_ind + 1]
                if prev_ind == -1 or (nums[ind] > nums[prev_ind]):
                    # take
                    lenn = max(lenn, 1 + prev[ind + 1])

                curr[prev_ind + 1] = lenn

            prev = curr

        return prev[0]


class BinarySearchLIS:
    def binary_search(self, arr, item):
        low = 0
        high = len(arr) - 1
        ans = len(arr)
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= item:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def LIS(self, nums):
        items = [nums[0]]
        lenn = 1
        for item in nums:
            if item > items[-1]:
                items.append(item)
                lenn += 1
            else:
                ind = self.binary_search(items, item)
                items[ind] = item

        return lenn


s = BinarySearchLIS()

k1 = s.LIS([10, 9, 2, 5, 3, 7, 101, 18])

k2 = s.LIS([0, 1, 0, 3, 2, 3])

print(k1)
print(k2)
