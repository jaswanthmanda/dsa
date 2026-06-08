# Two Sum


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map
        hash_map = {}

        for i, item in enumerate(nums):
            rem = target - item
            if rem in hash_map:
                return [hash_map[rem], i]

            hash_map[item] = i

        return []
