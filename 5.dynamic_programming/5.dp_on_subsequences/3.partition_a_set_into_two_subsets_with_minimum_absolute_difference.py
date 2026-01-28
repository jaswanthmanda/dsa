# Partition a set into two subsets with minimum absolute difference
"""
Given an array arr of n integers, 
partition the array into two subsets such that the absolute difference between their sums is minimized.
"""
"""
Example 1:
Input: arr = [1, 7, 14, 5]
Output: 1
Explanation: The array can be partitioned as [1, 7, 5] and [14], with an absolute difference of 1.


Example 2:
Input: arr = [3, 1, 6, 2, 2]
Output: 0
Explanation: The array can be partitioned as [3, 2, 2] and [6, 1], with an absolute difference of 0.
"""
"""
Constraints:
- 1 ≤ n * sum of array elements ≤ 106
- 0 < arr[i] <= 10^4
"""


class Solution:
    def kk_return(self, n, arr, target):
        prev, curr = [False] * (target + 1), [False] * (target + 1)
        prev[0] = True

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

        return prev

    def minDifference(self, arr, n):
        if n < 2:
            return 0

        total_sum = sum(arr)

        j = total_sum // 2

        possible = self.kk_return(n, arr, j)

        for s in range(j, -1, -1):
            if possible[s]:
                return total_sum - s * 2


s = Solution()

k1 = s.minDifference([1, 7, 14, 5], 4)

k2 = s.minDifference([3, 1, 6, 2, 2], 5)

print(k1)
print(k2)
