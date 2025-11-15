from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        N = len(nums)
        nice_arrays_count = 0
        odd_counter = 0
        while j < N:
            print(i, j, nums[i : j + 1], odd_counter, end=" ")
            if odd_counter < k:
                if nums[j] % 2 != 0:
                    odd_counter += 1
                j += 1
            elif odd_counter == k:
                nice_arrays_count += 1
                if nums[j] % 2 != 0:
                    odd_counter += 1
                j += 1
            else:
                while odd_counter > k and i < j:
                    if nums[i] % 2 != 0:
                        odd_counter -= 1
                    i += 1
            print(nice_arrays_count)

        return nice_arrays_count


Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3)
