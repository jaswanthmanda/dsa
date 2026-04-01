# Combination Sum


class Solution(object):
    def f(self, ind, arr, target, ans, ds):
        if ind == len(arr):
            if target == 0:
                ans.append(ds[:])
            return

        if arr[ind] <= target:
            ds.append(arr[ind])
            self.f(ind, arr, target - arr[ind], ans, ds)
            ds.pop()

        self.f(ind + 1, arr, target, ans, ds)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        self.f(0, candidates, target, ans, [])
        return ans
