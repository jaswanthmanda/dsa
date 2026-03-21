# Prefix Sum

"""
When to think prefix sum (signals)
- count subarrays
- subarray sum = k
- sum divisible by k
- equal 0s and 1s
- anything with running total + past info

Core idea:
- if current sum = S, look for previous sum = S - k
"""


def count_subarrays(nums, k):
    prefix_sum = 0
    count = 0
    freq = {0: 1}  # important

    for num in nums:
        prefix_sum += num

        if (prefix_sum - k) in freq:
            count += prefix_sum[prefix_sum - k]

        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count


"""
Patterns:
- sum = k (prefix sum +  hashmap)
- sum divisible by k (prefix % k)
- equal 0s & 1s (treat 0 -> -1)
- binary sum (prefix OR atMost trick)
"""
"""
3 - step logic:
1. Maintain prefix_sum
2. Check: what previous value do I need?
3. Store current in hashmap
"""
"""
Oneline: prefix sum + hashmap = number/count of subarrays
"""
