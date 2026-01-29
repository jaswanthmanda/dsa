# Count partitions with given difference
"""
Given an array arr of n integers and an integer diff,
count t  he number of ways to partition the array into two subsets S1 and S2 such that:
|S1-S2| = diff and S1 ≥ S2
Where |S1| and |S2| are sum of Subsets S1 and S2 respectively.

Return the result modulo 109 + 7.

Note: A partition means that the union of S1 and S2 is the original array,
and no element is left out or used twice — every element of the array belongs to exactly one of the two subsets.
"""
"""
Example 1:
Input: arr = [1, 1, 2, 3], diff = 1
Output: 3
Explanation: The subsets are [1, 2] and [1, 3], [1, 3] and [1, 2], [1, 1, 2] and [3].


Example 2:
Input: arr = [1, 2, 3, 4], diff = 2
Output: 2
Explanation: The subsets are [1, 3] and [2, 4], [1, 2, 3] and [4].
"""
"""
Constraints:
- 1 <= n <= 200
- 0 <= d <= 104
- 0 <= arr[i] <= 50
"""


class Solution:
    def f(self, ind, su, arr, dp):
        if ind < 0:
            return 1 if su == 0 else 0

        if dp[ind][su] != -1:
            return dp[ind][su]

        take = 0
        if arr[ind] <= su:
            take = self.f(ind - 1, su - arr[ind], arr, dp)
        not_take = self.f(ind - 1, su, arr, dp)

        dp[ind][su] = (take + not_take)

        return take + not_take

    def countPartitions(self, n, diff, arr):
        MOD = (10**9) + 7

        totalSum = sum(arr)

        # IMPORTANT CHECK
        if (totalSum - diff) % 2 != 0 or totalSum < diff:
            return 0

        target = (totalSum - diff) // 2

        dp = [[-1] * (target + 1) for _ in range(n)]

        ans = self.f(n - 1, target, arr, dp)

        return ans % MOD


class SolutionOptimal:
    def countPartitions(self, n, diff, arr):
        MOD = (10**9) + 7

        totalSum = sum(arr)

        # IMPORTANT CHECK
        if (totalSum - diff) % 2 != 0 or totalSum < diff:
            return 0

        target = (totalSum - diff) // 2

        dp = [[0] * (target + 1) for _ in range(n)]

        # handle base cases
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if arr[0] != 0 and arr[0] < target:
            dp[0][arr[0]] = 1

        for ind in range(1, n):
            for tar in range(target + 1):
                take = 0
                if arr[ind] <= tar:
                    take = dp[ind - 1][tar - arr[ind]]
                not_take = dp[ind - 1][tar]

                dp[ind][tar] = (take + not_take)

        return dp[n - 1][target] % MOD


class SolutionOptimalSpace:
    def countPartitions(self, n, diff, arr):
        MOD = (10**9) + 7

        totalSum = sum(arr)

        # IMPORTANT CHECK
        if (totalSum - diff) % 2 != 0 or totalSum < diff:
            return 0

        target = (totalSum - diff) // 2

        prev, curr = [0] * (target + 1), [0] * (target + 1)

        # handle base cases
        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1

        if arr[0] != 0 and arr[0] < target:
            prev[arr[0]] = 1

        for ind in range(1, n):
            curr = [0] * (target + 1)
            for tar in range(target + 1):
                take = 0
                if arr[ind] <= tar:
                    take = prev[tar - arr[ind]]
                not_take = prev[tar]

                curr[tar] = (take + not_take)

            prev = curr

        return prev[target] % MOD


s = SolutionOptimalSpace()

k1 = s.countPartitions(
    4,
    1,
    [1, 1, 2, 3],
)

k2 = s.countPartitions(
    4,
    2,
    [1, 2, 3, 4],
)

print(k1)
print(k2)
