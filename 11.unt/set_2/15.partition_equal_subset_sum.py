# Partition equal subset sum
from typing import List


class Solution:
    def f(self, i, target, nums, dp):
        if target == 0:
            return True

        if i < 0:
            return False

        if dp[i][target] != -1:
            return dp[i][target]

        take = False
        if nums[i] <= target:
            take = self.f(i - 1, target - nums[i], nums, dp)
        notTake = self.f(i - 1, target, nums, dp)

        dp[i][target] = take or notTake

        return dp[i][target]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False

        targetVal = totalSum // 2

        dp = [[-1 for _ in range(targetVal + 1)] for _ in range(n)]

        return self.f(n - 1, targetVal, nums, dp)


class SolutionOptimal:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False

        targetVal = totalSum // 2

        dp = [[False for _ in range(targetVal + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, targetVal + 1):
                notTake = dp[i - 1][j]
                take = False
                if nums[i - 1] <= j:
                    take = dp[i - 1][j - nums[i - 1]]

                dp[i][j] = take or notTake

        return dp[n][targetVal]


class SolutionOptimalSpace:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False

        targetVal = totalSum // 2

        prev = [False] * (targetVal + 1)

        prev[0] = True

        for i in range(1, n + 1):
            curr = [False] * (targetVal + 1)
            curr[0] = True
            for j in range(1, targetVal + 1):
                notTake = prev[j]
                take = False
                if nums[i - 1] <= j:
                    take = prev[j - nums[i - 1]]

                curr[j] = take or notTake

            prev = curr

        return prev[targetVal]
