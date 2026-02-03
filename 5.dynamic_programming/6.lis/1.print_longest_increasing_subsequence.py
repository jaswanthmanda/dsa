# Print longest increasing subsequence
"""
Given an array of n integers arr, return the Longest Increasing Subsequence (LIS) that is Index-wise Lexicographically Smallest.

The Longest Increasing Subsequence (LIS) is the longest subsequence where all elements are in strictly increasing order.

A subsequence A1 is Index-wise Lexicographically Smaller than another subsequence A2 if,
at the first position where A1 and A2 differ,
the element in A1 appears earlier in the array arr than corresponding element in S2.

Your task is to return the LIS that is Index-wise Lexicographically Smallest from the given array.
"""
"""
Example 1:
Input: arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
Output: [10, 22, 33, 50, 60, 80]
Explanation: The LIS is [10, 22, 33, 41, 60, 80] and it is the index-wise lexicographically smallest.


Example 2:
Input: arr = [1, 3, 2, 4, 6, 5]
Output: [1, 3, 4, 6]
Explanation: Possible LIS sequences are [1, 3, 4, 6] and [1, 2, 4, 6].
Since [1, 3, 4, 6] is Index-wise Lexicographically Smaller, it is the result.
"""
"""
Constraints:
- 1 <= arr.length <= 103
- -106 <= arr[i] <= 106
"""


class Solution:
    def longestIncreasingSubsequence(self, arr):
        n = len(arr)

        ans = []
        dp = [1] * n
        parent = [0] * n

        lastIndex = 0

        maxLen = 0

        for i in range(n):
            parent[i] = i

            for prevInd in range(i):

                if arr[prevInd] < arr[i]:

                    if dp[i] < dp[prevInd] + 1:
                        dp[i] = dp[prevInd] + 1
                        parent[i] = prevInd

                    elif dp[i] == dp[prevInd] + 1 and prevInd < parent[i]:
                        parent[i] = prevInd

            if dp[i] > maxLen:
                lastIndex = i
                maxLen = dp[i]

        i = lastIndex
        while parent[i] != i:
            ans.append(arr[i])

            i = parent[i]

        ans.append(arr[i])

        ans.reverse()

        return ans


s = Solution()

k1 = s.longestIncreasingSubsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])

k2 = s.longestIncreasingSubsequence([1, 3, 2, 4, 6, 5])


print(k1)
print(k2)
