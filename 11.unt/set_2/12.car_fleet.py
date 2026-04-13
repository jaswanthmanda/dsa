# Car Fleet
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p1, p2) for p1, p2 in zip(position, speed)]

        stack = []
        for tm, spd in sorted(pairs)[::-1]:
            # append the time they reach to stack
            stack.append((target - tm) / spd)

            # check for last item in stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
