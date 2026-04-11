# Linked list cycle
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# slow vs fast pointer


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # base case
        if not head:
            return False

        slow = head
        fast = head

        while fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
