# Find non repeating numbers
from sys import *
from collections import *
from collections import Counter
from math import *

"""
Sample Input 1:
2
4
2 4 7 2
8
3 9 3 1 4 8 1 9
Sample Output 1:
4 7
4 8
Explanation Of Sample Input 1:
Test Case 1: The given array is [ 2, 4, 7, 2 ].  4 and 7 are the two non-repeating numbers. Hence the output will be 4 and 7.


Test Case 2: Numbers 3, 1, 9 occurs two times while 4 and 8 occur once. Hence the output will be 4 8
Sample Input 2:
2
6
11 2 6 11 6 5
4
3 5 5 7
Sample Output 2:
2 5
3 7
"""


def findNonRepeatingBruteForce(arr):
    # Return a list of 2 integers
    # Write your code here
    # sort the list
    n = len(arr)

    if n in [0, 1, 2]:
        return arr

    arr.sort()

    res = []

    if arr[0] != arr[1]:
        res.append(arr[0])

    for i in range(1, n - 1):
        if arr[i] != arr[i - 1] and arr[i + 1] != arr[i]:
            res.append(arr[i])

    if arr[n - 2] != arr[n - 1]:
        res.append(arr[n - 1])

    return res


def findNonRepeating(arr):
    # Return a list of 2 integers
    # Write your code here
    n = len(arr)

    if n in [0, 1, 2]:
        return arr

    mp = Counter(arr)

    res = []

    for key, val in mp.items():
        if val == 1:
            res.append(key)

    return res
