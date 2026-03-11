# Palindrome linked list
"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""
"""
Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
"""
"""
Constraints:
- The number of nodes in the list is in the range [1, 105].
- 0 <= Node.val <= 9
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        ""
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head1 = head
        head2 = prev
        while head1 and head2:
            if head1.val != head2.val:
                return False

            head1 = head1.next
            head2 = head2.next

        return True
