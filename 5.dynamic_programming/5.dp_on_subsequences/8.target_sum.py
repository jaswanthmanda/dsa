# Target sum
"""
Given an array nums of n integers and an integer target,
build an expression using the integers from nums where each integer
can be prefixed with either a '+' or '-' sign.

The goal is to achieve the target sum by evaluating all possible combinations of these signs.

Determine the number of ways to achieve the target sum and return your answer with modulo 10^9+7.
"""
"""
Example 1:
Input: nums = [1, 2, 7, 1, 5], target = 4
Output: 2
Explanation: There are 2 ways to assign symbols to make the sum of nums be target 4.
+1 + 2 + 7 - 1 - 5 = 4
-1 + 2 + 7 + 1 - 5 = 4


Example 2:
Input: nums = [1], target = 1
Output: 1
Explanation: There is only one way to assign symbols to make the sum of nums be target 1.
"""
"""
Constraints:
- 1 ≤ n ≤ 100
- 0 ≤ nums[i] ≤ 1000
- 0 <= sum(A[i]) <= 104
- -1000 <= target <= 1000
"""


class Solution:
    def f(self, ind, target, nums, dp):
        if ind < 0:
            if target == 0:
                return 1
            return 0

        # print(ind, target, nums[ind])
        if dp[ind][target + 1000] != -1:
            return dp[ind][target + 1000]

        pos = self.f(ind - 1, target + nums[ind], nums, dp)
        neg = self.f(ind - 1, target - nums[ind], nums, dp)

        dp[ind][target + 1000] = pos + neg

        return pos + neg

    def targetSum(self, n, target, nums):
        # totalSum = sum(nums)
        MOD = (10**9) + 7
        dp = [[-1] * (10**4 + 1) for _ in range(n)]
        ans = self.f(n - 1, target, nums, dp)
        return ans % MOD


class SolutionOptimal:
    """It is basically twisted count subarray sum problem actually have to find the pattern"""

    def kk_return(self, arr, n, k):
        MOD = (10**9) + 7
        prev, curr = [0] * (k + 1), [0] * (k + 1)

        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1

        if arr[0] != 0 and arr[0] <= k:
            prev[arr[0]] = 1

        for ind in range(1, n):
            curr = [0] * (k + 1)
            for tar in range(k + 1):
                take = 0
                not_take = prev[tar]
                if arr[ind] <= tar:
                    take = prev[tar - arr[ind]]

                curr[tar] = take + not_take
            prev = curr

        return prev[k] % MOD

    def targetSum(self, n, target, nums):
        if target < 0:
            return 0
        return self.kk_return(nums, n, target)


s = SolutionOptimal()

k1 = s.targetSum(
    5,
    4,
    [1, 2, 7, 1, 5],
)

k2 = s.targetSum(
    1,
    1,
    [1],
)

k3 = s.targetSum(
    3,
    -22,
    [22, 21, 4],
)

print(k1)
print(k2)
print(k3)
