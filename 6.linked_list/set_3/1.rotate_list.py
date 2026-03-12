# Rotate List
"""
Given the head of a linked list, rotate the list to the right by k places.
"""
"""
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""
"""
Constraints:
- The number of nodes in the list is in the range [0, 500].
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 109
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # base case
        if head is None:
            return head

        ll = 0
        temp = head
        while temp:
            ll += 1
            temp = temp.next

        k %= ll
        if k == 0:
            return head

        kemp = ll - k
        temp = head

        for _ in range(kemp - 1):
            temp = temp.next

        nextNode = temp.next
        temp.next = None

        temp = nextNode

        while temp.next is not None:
            temp = temp.next

        temp.next = head

        return nextNode

    def rotateRightOptimal2Pass(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # base case
        if head is None or head.next is None:
            return head

        # find the length of ll
        ll = 1
        temp = head
        while temp.next:
            temp = temp.next
            ll += 1

        k %= ll
        if k == 0:
            return head

        # make circular
        temp.next = head

        # find the new tail
        steps = ll - k - 1
        newTail = head
        for _ in range(steps):
            newTail = newTail.next

        newHead = newTail.next

        # break circle
        newTail.next = None

        return newHead
