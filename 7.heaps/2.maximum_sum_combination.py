# Maximum sum comnbination
import heapq


class Solution:
    def maxSumCombinations(self, nums1, nums2, k):
        # insert items
        nums1.sort(reverse=True)
        nums2.sort(reverse=True)

        heap = []
        visited = set()

        heapq.heappush(heap, (-(nums1[0], nums2[0]), 0, 0))
        visited.add((0, 0))

        ans = []

        while k != 0:
            s, i, j = heapq.heappop(heap)
            ans.append(-s)

            if (i + 1, j) not in visited and i + 1 < len(nums1):
                heapq.heappush(heap, (-(nums1[i + 1] + nums2[j]), i + 1, j))
                visited.add((i + 1, j))

            if (i, j + 1) not in visited and j + 1 < len(nums2):
                heapq.heappush(heap, (-(nums1[i], nums2[j + 1]), i, j + 1))
                visited.add((i, j + 1))

            k -= 1

        return ans
