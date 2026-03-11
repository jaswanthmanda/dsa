# Remove nth node from End of the ll
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
"""
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""
"""
Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None

        ll = 0

        temp = head
        while temp:
            ll += 1
            temp = temp.next

        if ll - n < 0:
            return head

        temp = head
        kemp = ll - n
        if kemp == 0:
            return head.next

        prev = None
        while temp.next is not None and kemp != 0:
            prev = temp
            kemp -= 1
            temp = temp.next

        if prev:
            prev.next = temp.next
        temp = temp.next

        return head

    def twoPassPattern(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        for _ in range(n):
            if fast.next is None:
                return head
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        if slow.next:
            slow.next = slow.next.next

        return dummy.next
