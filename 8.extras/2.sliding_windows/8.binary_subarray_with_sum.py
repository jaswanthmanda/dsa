# Binary subarray with sum k

# best approach: prefix_sum + hash_map


class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefix_sum = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - goal in freq:
                count += freq[prefix_sum - goal]

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count
