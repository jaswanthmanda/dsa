class BinarySearch:

    def __init__(self):
        pass

    def search_iter(self, arr: list, ele: int) -> int:
        """Iterative binary search alogrithm (must pass sorted arr)"""
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] == ele:
                return mid
            elif arr[mid] < ele:
                low = mid + 1
            elif arr[mid] > ele:
                high = mid - 1
        return -1

    def search_rec(self, arr: list, x: int, low: int, high: int) -> int:
        """Recursive binary search algorithm"""
        if low > high:
            return -1

        mid = (low + high)//2
        if arr[mid] == x:
            return mid
        if x < arr[mid]:
            return self.search_rec(arr, x, low, mid - 1)
        if x > arr[mid]:
            return self.search_rec(arr, x, mid + 1, high)


# function calls
cls_obj = BinarySearch()
# print(cls_obj.search_iter([1, 2, 3, 4, 5, 6], 8))
print(cls_obj.search_rec([1, 2, 3, 4, 5, 6], 5, 0, 5))
