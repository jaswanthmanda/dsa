# Top k frequent elements
from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # n
        n = len(nums)

        if k > n:
            return -1

        # mp
        mp = Counter(nums)

        pq = []

        for item, count in mp.items():
            heapq.heappush(pq, (-1 * count, -1 * item))

        curr = 0
        result = []
        while curr != k:
            _, val = heapq.heappop(pq)

            result.append(-1 * val)

            curr += 1

        return result
