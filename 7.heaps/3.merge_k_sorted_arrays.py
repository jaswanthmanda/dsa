# Merge k sorted arrays

import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # base case
        n = len(lists)
        heap = []

        def add_list_items_to_heap(lst):
            while lst is not None:
                heapq.heappush(heap, lst.val)
                lst = lst.next

        for i in range(n):
            add_list_items_to_heap(lists[i])

        new_node = None

        if heap:
            val = heapq.heappop(heap)
            new_node = ListNode(val)
            prev = new_node
            while heap:
                val = heapq.heappop(heap)
                temp_node = ListNode(val)
                prev.next = temp_node
                prev = prev.next

        return new_node

    def mergeKListsOptimal(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # base case
        n = len(lists)
        heap = []

        # put first node of each node in list
        for i in range(n):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        prev = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            prev.next = node
            prev = prev.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
