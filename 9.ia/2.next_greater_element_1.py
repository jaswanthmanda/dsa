# next greater element 1


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        mp = {}

        # process nums2
        for x in nums2:
            while stack and x > stack[-1]:
                mp[stack.pop()] = x

            stack.append(x)

        # process stack items
        for x in stack:
            mp[x] = -1

        return [mp[x] for x in nums1]
