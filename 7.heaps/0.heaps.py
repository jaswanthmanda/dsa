# Heaps Starter

"""
When to think of heaps (signals)
- kth smallest / kth largest
- top k frequent
- closest k elements
- merge k sorted lists
- stream of numbers (running median / kth largest)

Core idea:
- keep only the best k elements using a heap
"""
import heapq


# min heap
x = 1
heap = []
heapq.heappush(heap, x)
heapq.heappop(heap)

# max heap -> use negative
x = 1
heapq.heappush(heap, -x)


# templates


# Top k largest
def topK(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return h


# kth largest (1-liner style)
def kth(nums, k):
    return heapq.nlargest(k, nums)[-1]


# Max heap when needed
heap = []
value1, value2 = 1, 2  # (example)
heapq.heappush(heap, (-value1, value2))  # store not

# pop max
_, val = heapq.heappop(heap)

"""
Patterns to remember:
- kth largest (min heap size k)
- kth smallest (max heap size k)
- top k freq (min heap)
- streaming kth (min heap)
- median (2 heaps)
"""
"""
3-step logic:
1. Do i need top k / smallest / largest
2. Use heap of size k
3. Remove extra elements
"""
"""
One-line: Heap best k elements efficiently
"""
"""
Complexity:
- Push/Pop -> O(log k)
- Total -> O(n log k)
"""
