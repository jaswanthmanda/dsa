# Permutation in a string
from os import *
from sys import *
from collections import *
from math import *


def findPermutations(s):
    if len(s) == 1:
        return [s]

    # Write your code here.
    n = len(s)

    s_list = list(s)

    res = []
    for i in range(n):
        x = s_list[i]

        remaining = s_list[:i] + s_list[i + 1 :]

        rem_str = "".join(remaining)

        perms = findPermutations(rem_str)

        for p in perms:
            res_list = x + p
            res.append(res_list)

    return res
