"""
Merge Two Sorted Lists:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

"""
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
"""
Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return None

        start1 = list1
        start2 = list2
        ans = None
        if start1:
            if start2:
                if start1.val <= start2.val:
                    ans = ListNode(start1.val)
                    start1 = start1.next
                else:
                    ans = ListNode(start2.val)
                    start2 = start2.next
            else:
                return start1
        elif start2:
            ans = ListNode(start2.val)
            start2 = start2.next

        finalans = ans

        while start1 is not None and start2 is not None:
            if start1.val <= start2.val:
                temp_node = ListNode(start1.val)
                ans.next = temp_node
                start1 = start1.next
                ans = ans.next
            else:
                temp_node = ListNode(start2.val)
                ans.next = temp_node
                start2 = start2.next
                ans = ans.next

        while start1:
            temp_node = ListNode(start1.val)
            ans.next = temp_node
            start1 = start1.next
            ans = ans.next

        while start2:
            temp_node = ListNode(start2.val)
            ans.next = temp_node
            start2 = start2.next
            ans = ans.next

        return finalans

    def mergeTwoListsSpaceOpt(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next
