from os import *
from sys import *
from collections import *
from math import *


def maximumValue(items, n, w):

    # Write your code here.
    # ITEMS contains [weight, value] pairs.

    # calc value per unit weight
    val_unit_wt = []
    for wt, val in items:
        val_unit_wt.append(val / wt)

    end_res = []

    for i, item in enumerate(items):
        wt, val = item
        val_per_wt = val_unit_wt[i]

        end_res.append((val, wt, val_per_wt))

    end_res.sort(reverse=True, key=lambda x: x[2])

    final_val = 0

    for item in end_res:
        if w == 0:
            break
        val, wt, val_per_wt = item
        if wt <= w:
            final_val += val
            w -= wt
        else:
            take = w
            final_val += val_per_wt * take

            break

    return final_val
