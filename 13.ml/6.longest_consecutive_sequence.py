# Longest consecutive Sequence

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3


Constraints:
- 0 <= nums.length <= 105
- - 109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def longestConsecutive(
        self,
        nums: List[int],
    ) -> int:
        # edge case
        if len(nums) == 0:
            return 0

        sett = set(nums)

        max_trc = float("-inf")

        for item in sett:
            if item - 1 not in sett:
                curr = 1
                i = item + 1
                while i in sett:
                    curr += 1
                    i += 1
                max_trc = max(max_trc, curr)

        return max_trc if max_trc != float("-inf") else 0


"""
TC: O(n)
SC: O(n)
"""
