# Two Sum
from typing import List


class Solution:
    def twoSum(
        self,
        nums: List[int],
        target: int,
    ) -> List[int]:
        # hash map
        hash_map = {}

        for i, item in enumerate(nums):
            rem = target - item
            if rem in hash_map:
                ind0 = hash_map[rem]
                return [ind0, rem]

            hash_map[item] = i

        return []
