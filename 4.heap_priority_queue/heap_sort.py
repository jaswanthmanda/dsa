# Implementation Basic.


def maxHeapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 1
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, n, largest)


def buildHeap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        maxHeapify(arr, n, i)


def heapSort(arr):
    n = len(arr)
    arr = buildHeap(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxHeapify(arr, i, 0)
