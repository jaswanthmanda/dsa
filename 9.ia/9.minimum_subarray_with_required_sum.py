# Sum of subarray minimums

"""
Sample Input 1:
4 13
13 7 6 12
Sample Output 1:
13 7
Explanation For Sample Input 1:
Out of all the subarrays, we have [13, 7] and [6, 12] with minimum length of 2 and sum of their elements greater than X = 13. As the starting index of [13, 7] is lower, we print it as the output.

Sample Input 2:
5 6
1 2 3 4 5
Sample Output 2:
3 4
"""


def minSubarray(arr, n, x):
    # Write your code here.
    if n == 0:
        return []

    if n == 1:
        return arr if arr[0] > x else []

    i = 0
    j = 0
    summ = 0
    start_index = n
    min_len = n + 1
    for j in range(n):
        summ += arr[j]

        while summ > x:
            curr_len = j - i + 1
            if curr_len < min_len:
                min_len = j - i + 1
                start_index = i
            elif curr_len == min_len:  # tie case
                start_index = min(start_index, i)
            summ -= arr[i]
            i += 1

    if start_index == n:
        return []

    return arr[start_index: start_index + min_len]
