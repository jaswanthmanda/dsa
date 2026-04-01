# Binary Numbers
from os import *
from sys import *
from collections import *
from math import *


def countSetBits(n):

    # Write your Code here.
    # Return an integer denoting the answer.
    kk = bin(n)
    kk = list(kk[2:])

    count_ones = 0

    for i in range(len(kk)):
        if kk[i] == "1":
            count_ones += 1

    return count_ones
