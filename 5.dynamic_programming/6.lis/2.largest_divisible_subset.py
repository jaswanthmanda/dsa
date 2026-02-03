# Largest divisible subset
"""
Given an array nums of positive integers, the task is to find the
largest subset such that every pair (a, b) of elements in the subset satisfies a % b == 0 or b % a == 0.

Return the subset in any order. If there are multiple solutions, return any one of them.

Note: As there can be multiple correct answers, the compiler returns 1 if the answer is valid, else 0.
"""
"""
Example 1:
Input: nums = [3, 5, 10, 20]
Output: [5, 10, 20]
Explanation:
The subset [5, 10, 20] satisfies the divisibility condition: 10 % 5 == 0 and 20 % 10 == 0.


Example 2:
Input: nums = [16, 8, 2, 4, 32]
Output: [2, 4, 8, 16, 32]
Explanation:
The entire array forms a divisible subset since 32 % 16 == 0, 16 % 8 == 0, and so on.
"""
"""
Constraints
- 1 <= nums.length <= 103
- 1 <= nums[i] <= 106
"""


class Solution:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums.sort()

        dp = [1] * n
        parent = [0] * n

        maxLen = 0
        lastIndex = 0

        for i in range(n):
            parent[i] = i
            for prevInd in range(i):
                if nums[i] % nums[prevInd] == 0:
                    if dp[i] < dp[prevInd] + 1:
                        dp[i] = dp[prevInd] + 1
                        parent[i] = prevInd

                    elif dp[i] == dp[prevInd] and prevInd < parent[i]:
                        parent[i] = prevInd

            if dp[i] > maxLen:
                maxLen = dp[i]
                lastIndex = i

        ans = []
        i = lastIndex
        while parent[i] != i:
            ans.append(nums[i])
            i = parent[i]

        ans.append(nums[i])
        # ans.reverse()

        return ans


s = Solution()

k1 = s.largestDivisibleSubset([3, 5, 10, 20])

k2 = s.largestDivisibleSubset([16, 8, 2, 4, 32])

k3 = s.largestDivisibleSubset([7, 14, 28, 3])

k4 = s.largestDivisibleSubset(
    [
        255,
        741,
        711,
        54,
        72,
        324,
        637,
        60,
        109,
        163,
        881,
        90,
        114,
        18,
        72,
        396,
        556,
        222,
        167,
        120,
        496,
        81,
        27,
        322,
        96,
        120,
        715,
        322,
        319,
        518,
        264,
        6,
        193,
        54,
        66,
        997,
        608,
        874,
        480,
        102,
        872,
        115,
        656,
        298,
        315,
        66,
        792,
    ],
)

print(k1)
print(k2)
print(k3)
print(k4)
