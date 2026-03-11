# Add two numbers
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
"""
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
"""
Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        start1 = l1
        start2 = l2
        carry = 0

        temp = None

        while start1 is not None and start2 is not None:
            val = start1.val + start2.val + carry
            temp_node = ListNode(val % 10)
            carry = val // 10
            if temp is None:
                ans = temp_node
                temp = ans
            else:
                temp.next = temp_node
                temp = temp.next

            start1 = start1.next
            start2 = start2.next

        while start1 is not None:
            val = start1.val + carry
            temp_node = ListNode(val % 10)
            carry = val // 10

            if temp is None:
                ans = temp_node
                temp = ans
            else:
                temp.next = temp_node
                temp = temp.next

            start1 = start1.next

        while start2 is not None:
            val = start2.val + carry
            temp_node = ListNode(val % 10)
            carry = val // 10

            if temp is None:
                ans = temp_node
                temp = ans
            else:
                temp.next = temp_node
                temp = temp.next

            start2 = start2.next

        if carry != 0:
            temp.next = ListNode(carry)

        return ans

    def addTwoNumbersReadable(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            temp.next = ListNode(total % 10)
            temp = temp.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
