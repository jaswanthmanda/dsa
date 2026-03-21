# Count number of subarrays


class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count_odd = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            if num % 2 != 0:
                count_odd += 1

            if count_odd - k in freq:
                count += freq[count_odd - k]

            freq[count_odd] = freq.get(count_odd, 0) + 1

        return count
