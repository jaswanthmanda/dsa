def merge_sort(nums1, nums2):
    start1 = 0
    start2 = 0
    end1 = len(nums1)
    end2 = len(nums2)

    temp = []

    while start1 < end1 and start2 < end2:
        if nums1[start1] <= nums2[start2]:
            temp.append(nums1[start1])
            start1 += 1
        else:
            temp.append(nums2[start2])
            start2 += 1

    while start1 < end1:
        temp.append(nums1[start1])
        start1 += 1

    while start2 < end2:
        temp.append(nums2[start2])
        start2 += 1

    return temp


def updated_mis(list1, list2):
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


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_sort_list(node1, node2):
    start1 = node1
    start2 = node2
    ans = None
    if start1:
        if start1.val <= start2.val:
            ans = ListNode(start1.val)
            start1 = start1.next
        else:
            ans = ListNode(start2.val)
            start2 = start2.next
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
        ans = temp_node

    while start2:
        temp_node = ListNode(start2.val)
        ans.next = temp_node
        ans = ans.next

    return finalans


nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

ans = merge_sort(nums1, nums2)
print(ans)
