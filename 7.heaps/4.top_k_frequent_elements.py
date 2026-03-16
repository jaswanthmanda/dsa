# Top k frequent elements
import heapq
from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_count = Counter(nums)

        heap = []

        for key, val in nums_count.items():
            heapq.heappush(heap, (-val, key))

        ans = []
        while k != 0:
            _, key = heapq.heappop(heap)
            ans.append(key)

            k -= 1

        return ans