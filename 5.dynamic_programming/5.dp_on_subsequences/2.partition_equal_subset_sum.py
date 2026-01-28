# Partition equal subset sum
"""
Given an array arr of n integers, return true if the array can be
partitioned into two subsets such that the sum of elements in both subsets is equal else return false.
"""
"""
Example 1:
Input: arr = [1, 10, 21, 10]
Output: True
Explanation: The array can be partitioned as [1, 10, 10] and [21].

Example 2:
Input: arr = [1, 2, 3, 5]
Output: False
Explanation: The array cannot be partitioned into equal sum subsets.
"""
"""
Constraints:
- 1 ≤ n ≤ 100
- 1 ≤ arr[i] ≤ 1000
- n*sum of elements ≤ 10^5
"""


class Solution:
    def f(self, ind, target, arr, dp):
        if target == 0:
            return True

        if ind < 0:
            return False

        if dp[ind][target] != -1:
            return dp[ind][target]

        take = False

        if arr[ind] <= target:
            take = self.f(ind - 1, target - arr[ind], arr, dp)
        not_take = self.f(ind - 1, target, arr, dp)

        dp[ind][target] = take or not_take

        return take or not_take

    def equalPartition(self, n, arr):
        total_sum = sum(arr)

        if total_sum % 2 != 0:
            return False

        kk = total_sum // 2

        dp = [[-1] * (kk + 1) for _ in range(n)]
        return self.f(n - 1, kk, arr, dp)


class SolutionOptimal:
    def kk_return(self, n, arr, target):
        dp = [[False] * (target + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        if arr[0] <= target:
            dp[0][arr[0]] = True

        for ind in range(1, n):
            for tar in range(1, target + 1):
                take = False

                if arr[ind] <= tar:
                    take = dp[ind - 1][tar - arr[ind]]
                not_take = dp[ind - 1][tar]

                dp[ind][tar] = take or not_take

        return dp[n - 1][target]

    def equalPartition(self, n, arr):
        if n < 2:
            return False

        total_sum = sum(arr)

        if total_sum % 2 != 0:
            return False

        kk = total_sum // 2

        return self.kk_return(n, arr, kk)


class SolutionOptimalSpace:
    def kk_return(self, n, arr, target):
        prev, curr = [False] * (target + 1), [False] * (target + 1)

        if arr[0] <= target:
            prev[arr[0]] = True

        for ind in range(1, n):
            curr = [False] * (target + 1)
            curr[0] = True
            for tar in range(1, target + 1):
                take = False

                if arr[ind] <= tar:
                    take = prev[tar - arr[ind]]
                not_take = prev[tar]

                curr[tar] = take or not_take

            prev = curr

        return prev[target]

    def equalPartition(self, n, arr):
        if n < 2:
            return False

        total_sum = sum(arr)

        if total_sum % 2 != 0:
            return False

        kk = total_sum // 2

        return self.kk_return(n, arr, kk)


s = SolutionOptimalSpace()

k1 = s.equalPartition(4, [1, 10, 21, 10])

k2 = s.equalPartition(4, [1, 2, 3, 5])

print(k1)
print(k2)
