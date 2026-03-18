# Sub array sum equals k
# Prefix sum + hashmap


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # main logic
        prefix_map = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in prefix_map:
                count += prefix_map[curr_sum - k]

            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1

        return count
