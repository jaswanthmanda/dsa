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
    def countPartitions(self, n, diff, arr):
