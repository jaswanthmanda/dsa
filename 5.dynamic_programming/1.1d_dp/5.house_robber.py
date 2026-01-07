# House Robber
"""
A robber is targeting to rob houses from a street. Each house has security
measures that alert the police when two adjacent houses are robbed.
The houses are arranged in a circular manner,
thus the first and last houses are adjacent to each other.

Given an integer array money, where money[i] represents the amount of money that can be looted from the (i+1)th house.
Return the maximum amount of money that the robber can loot without alerting the police.
"""
"""
Example 1:
Input: money = [2, 1, 4, 9]
Output: 10
Explanation:
[2, 1, 4, 9] The underlined houses would give the maximum loot.
Note that we cannot loot the 1st and 4th houses together.

Example 2:
Input: money = [1, 5, 2, 1, 6]
Output: 11
Explanation:
[1, 5, 2, 1, 6] The underlined houses would give the maximum loot.
"""
"""
Constraints:
- 1 <= money.length <= 105
- 0 <= money[i] <= 1000
"""


class Solution:
    def func(self, n, nums):
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2 = 0
        prev = 0

        for x in nums:
            curr = max(prev, prev2 + x)
            prev2 = prev
            prev = curr

        return prev

    def houseRobber(self, money):
        n = len(money)

        if n == 1:
            return money[0]

        temp1 = [money[i] for i in range(1, n)]
        temp2 = [money[i] for i in range(n - 1)]

        return max(self.func(n - 1, temp1), self.func(n - 1, temp2))


s = Solution()

k1 = s.houseRobber([2, 1, 4, 9])

k2 = s.houseRobber([1, 5, 2, 1, 6])

k3 = s.houseRobber([100])

print(k1)
print(k2)
print(k3)
