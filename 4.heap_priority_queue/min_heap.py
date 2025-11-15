import math


class MyMinHeap:
    def __init__(self):
        self.arr = []

    def parent(self, i):
        return (i - 1) // 2

    def lchild(self, i):
        return 2 * i + 1

    def rchild(self, i):
        return 2 * i + 2

    def insert(self, x):
        arr = self.arr
        arr.append(x)
        i = len(arr) - 1
        while i > 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]
            i = p

    def minHeapify(self, i):
        arr = self.arr
        lt = self.lchild(i)
        rt = self.rchild(i)
        smallest = i
        n = len(arr)
        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt
        if rt < n and arr[rt] < arr[smallest]:
            smallest = rt
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.minHeapify(smallest)

    def extractMin(self):
        arr = self.arr
        n = len(arr)
        if n == 0:
            return math.inf
        res = arr[0]
        arr[0] = arr[n - 1]  # instead of swapping, we assign
        arr.pop()
        self.minHeapify(0)
        return res

    def decreaseKey(self, i, x):
        arr = self.arr
        arr[i] = x
        while i != 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]
            i = p

    def delete(self, i):
        n = len(self.arr)
        if i >= n:
            return
        else:
            self.decreaseKey(i, -math.inf)
            self.extractMin()
