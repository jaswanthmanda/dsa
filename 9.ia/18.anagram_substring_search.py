# Anagram Substring Search

from sys import *
from collections import *
from math import *

from sys import stdin
import sys


def findAnagramsIndices(n, m, st, ptr):

    # Write your code here.
    


# Taking input using fast I/O.
def takeInput():

    nums = list(map(int, input().strip().split(" ")))
    st = input()
    ptr = input()

    return nums, st, ptr


# Main.
t = int(input())
while t:
    nums, st, ptr = takeInput()
    n, m = nums
    answer = findAnagramsIndices(n, m, st, ptr)
    for ans in answer:
        print(ans, end=" ")
    print()
    t = t-1
