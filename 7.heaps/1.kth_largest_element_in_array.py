# Kth largest element in array

import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # base case
        # n = len(nums)
        # if k > n:
        #     return None

        # q = []

        # for items in nums:
        #     heapq.heappush(q, -1 * items)

        # while k != 0:
        #     item = heapq.heappop(q)
        #     k -= 1

        # return -1 * item

        # optimal
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
