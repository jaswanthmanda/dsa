# Contains duplicates II
# [1, 2, 3, 1], k = 3,  otpt: true

from typing import List


class Solution:
    def containsNearbyDuplicate(
        self,
        nums: List[int],
        k: int,
    ) -> bool:
        # mp
        mp = {}

        for i, item in enumerate(nums):
            if item in mp:
                val = abs(i - mp[item])

                if val <= k:
                    return True

            mp[item] = i

        return False
