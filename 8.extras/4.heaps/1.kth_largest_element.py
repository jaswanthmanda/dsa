# Kth largest element
import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for item in nums:
            heapq.heappush(heap, item)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
