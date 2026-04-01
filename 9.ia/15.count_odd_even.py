# Count odd even
from collections import Counter


def countEvenOdd(arr, n):
    # Write your code here.
    count_mp = Counter(arr)

    odd_count = 0
    even_count = 0

    for key, val in count_mp.items():
        if val % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return [odd_count, even_count]