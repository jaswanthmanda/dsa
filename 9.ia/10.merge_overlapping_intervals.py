# Merge overlapping intervals

from os import *
from sys import *
from collections import *
from math import *

"""

    intervals[i][0] = start point of i'th interval
    intervals[i][1] = finish point of i'th interval

"""


def mergeIntervals(intervals):
    # Write your code here
    # base case
    if len(intervals) in [0, 1]:
        return intervals

    # sort the arr
    intervals.sort(key=lambda x: x[0])

    res = []

    # compare the intervals
    last_start = intervals[0][0]
    last_end = intervals[0][1]
    for start, end in intervals[1:]:
        if last_end >= start:
            last_end = max(last_end, end)
        else:
            res.append([last_start, last_end])
            last_start = start
            last_end = end

    res.append([last_start, last_end])
    return res
