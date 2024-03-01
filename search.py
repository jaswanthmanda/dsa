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


class FirstOccuredElemen(BinarySearch):

    def __init__(self) -> None:
        pass

    def main_fun_fir(self, arr: list, item: int) -> int:
        """Returns first occurence of the given item"""

        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high)//2
            if item < arr[mid]:
                high = mid - 1
            elif item > arr[mid]:
                low = mid + 1
            else:
                if mid == 0 or arr[mid - 1] != arr[mid]:
                    return mid
                else:
                    high = mid - 1
        return -1

class LastOccuredElemen(FirstOccuredElemen):

    def __init__(self) -> None:
        pass

    def main_fun_las(self, arr: list, item: int) -> int:
        """Return last occured element in the arr"""
        low = 0
        high = len(arr) - 1
        while low<=high:
            mid = (low + high)//2
            if item < arr[mid]:
                high = mid - 1
            elif item > arr[mid]:
                low = mid + 1
            else:
                if mid == len(arr) - 1 or arr[mid+1] != arr[mid]:
                    return mid
                else:
                    low = mid + 1

class CountNumberofOccured(LastOccuredElemen):

    def __init__(self):
        pass

    def count_occ_bin_search(self, arr: list, item: int):
        """Return number of occurences"""
        first = self.main_fun_fir(arr, item)

        if first == -1:
            return 0

        return self.main_fun_las(arr, item) - first + 1

# function calls
cls_obj = CountNumberofOccured()
# print(cls_obj.search_iter([1, 2, 3, 4, 5, 6], 8))
print(cls_obj.count_occ_bin_search([1, 2, 3, 4, 40, 40, 40, 50, 60], 40))