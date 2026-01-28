# Count subsets with sum k
"""
Given an array arr of n integers and an integer K, count the number of subsets
of the given array that have a sum equal to K.
Return the result modulo (109 + 7).
"""
"""
Example 1:
Input: arr = [2, 3, 5, 16, 8, 10], K = 10
Output: 3
Explanation: The subsets are [2, 8], [10], and [2, 3, 5].

Example 2:
Input: arr = [1, 2, 3, 4, 5], K = 5
Output: 3
Explanation: The subsets are [5], [2, 3], and [1, 4].
"""
"""
Constraints:
- 1 <= n <= 100
- 1 <= arr[i] <= 103
- 1 <= K <= 103
"""


class Solution:
    def kk_return(self, arr, n, k):
        MOD = (10**9) + 7
        dp = [[0] * (k + 1) for _ in range(n)]

        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if arr[0] != 0 and arr[0] <= k:
            dp[0][arr[0]] = 1

        for ind in range(1, n):
            for tar in range(k + 1):
                take = 0
                not_take = dp[ind - 1][tar]
                if arr[ind] <= tar:
                    take = dp[ind - 1][tar - arr[ind]]

                dp[ind][tar] = take + not_take

        return dp[n - 1][k] % MOD

    def perfectSum(self, arr, K):
        n = len(arr)

        ans = self.kk_return(arr, n, K)

        return ans


class SolutionOptimal:
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

    def perfectSum(self, arr, K):
        n = len(arr)

        ans = self.kk_return(arr, n, K)

        return ans


s = SolutionOptimal()

k1 = s.perfectSum(
    [2, 3, 5, 16, 8, 10],
    10,

)

k2 = s.perfectSum(
    [1, 2, 3, 4, 5],
    5,
)

print(k1)
print(k2)
