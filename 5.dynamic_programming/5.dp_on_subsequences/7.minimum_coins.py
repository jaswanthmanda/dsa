# Minimum coins
"""
Given an integer array of coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that are needed to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
There are infinite numbers of coins of each type
"""
"""
Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1. We need 3 coins to make up the amount 11.

Example 2:
Input: coins = [2, 5], amount = 3
Output: -1
Explanation: It's not possible to make amount 3 with coins 2 and 5. Since we can't combine the coin 2 and 5 to make the amount 3, the output is -1.
"""
"""
Constraints
- n = number of distinct denominations
- 1 <= n <= 100
- 1 <= coins[i],<= 10^3
- 0 <= amount <= 10^3
"""


class Solution:
    def MinimumCoins(self, coins, amount): ...
