# Adjacent 1 diff subsequence
from collections import Counter


def scripts(nums):
    freq = Counter(nums)
    ans = 0

    # base logic
    """
    Where we will have
    """
    for x in freq:
        ans = max(ans, freq.get(x - 1, 0) + freq[x] + freq.get(x + 1, 0))

    return ans


k1 = scripts([4, 3, 5, 1, 2, 2, 1])  # expc:5
k2 = scripts([3, 7, 5, 1, 5])  # expc:2
k3 = scripts([2, 2, 3, 2, 1, 2, 2])  # expc: 7
print(k1)
print(k2)
print(k3)
