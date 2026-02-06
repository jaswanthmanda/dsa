# Longest biotonic sequence
"""
Given an array arr of n integers, the task is to find the length of the longest bitonic sequence.
A sequence is considered bitonic if it first increases, then decreases.
The sequence does not have to be contiguous.
"""
"""
Example 1:
Input: arr = [5, 1, 4, 2, 3, 6, 8, 7]
Output: 6
Explanation: The longest bitonic sequence is [1, 2, 3, 6, 8, 7] with length 6.

Example 2:
Input: arr = [10, 20, 30, 40, 50, 40, 30, 20]
Output: 8
Explanation: The entire array is bitonic, increasing up to 50 and then decreasing.
"""
"""
Constraints:
- 1 <= arr.length <= 103
- -106<= arr[i] <= 106
"""


class Solution:
    def kemp(self, arr):
        n = len(arr)

        dp = [1] * n

        for i in range(n):
            for prevInd in range(i):
                if arr[i] > arr[prevInd]:
                    if dp[i] < dp[prevInd] + 1:
                        dp[i] = dp[prevInd] + 1

        return dp

    def LongestBitonicSequence(self, arr):
        if len(arr) < 2:
            return 0

        n = len(arr)

        dp1 = self.kemp(arr)
        arr.reverse()
        dp2 = self.kemp(arr)
        dp2.reverse()

        max_len = 0
        for i in range(n):
            max_len = max(max_len, dp1[i] + dp2[i] - 1)

        return max_len


s = Solution()

k1 = s.LongestBitonicSequence(
    [5, 1, 4, 2, 3, 6, 8, 7],
)

k2 = s.LongestBitonicSequence(
    [10, 20, 30, 40, 50, 40, 30, 20],
)

print(k1)
print(k2)
