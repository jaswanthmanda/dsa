class ListNode:

    def __init__(self, key):
        self.key = key
        self.next = None


items = [5, 20, 20, 15, 30, 30, 30, 25, 40]

node = ListNode(10)

head = node

for item in items:
    node.next= ListNode(item)
    node = node.next


# prints the linked list
def printlist(head: ListNode) -> None:
    while head:
        print(head.key)
        head = head.next

# search functionality
def search_item(integer: int, head: ListNode):

    counter = 0
    while head:
        counter+=1
        if head.key == integer:
            return counter
        head = head.next

    return -1

# inserts node at the begin of the list
def insert_node_at_begin(integer: int, head: ListNode):
    start_node = ListNode(integer)
    start_node.next = head
    return start_node

# inserts node at the end
def insert_node_at_end(integer: int, head: ListNode):
    end_node = ListNode(integer)
    if head == None:
        return end_node
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = end_node

    return head

def insert_node_at_given_pos(integer: int, post: int, head: ListNode):
    """Inserts node at the given pos"""
    insert_node = ListNode(integer)
    counter = 1
    if head is None:
        return insert_node
    if post == 1:
        insert_node.next = head
        return insert_node
    else:
        curr = head
        while curr:
            counter += 1
            if counter == post:
                insert_node.next = curr.next
                curr.next = insert_node  # 10 5 (14)
            curr = curr.next
    return head

def delete_node_at_start(head: ListNode):
    """Deletes starting node."""
    if head and head.next:
        head = head.next
        return head
    return head

def delete_last_node(head: ListNode):
    """deletes last node"""
    if head is None or head.next is None:
        return None
    curr = head
    while curr:
        if curr.next.next is None:
            curr.next = None  # 10 5 15 20
            break
        curr = curr.next
    return head

def delete_node_from_middle_with_add(node: ListNode, head: ListNode):
    """deletes node from middle with address of the middle node"""
    # 10->5->15->20->12->None
    node = node.next
    node.next = node.next.next
    return head

def insert_element_in_sorted_list(integer: int, head: ListNode):
    """Inserts element in sorted list."""
    new_node = ListNode(integer)
    if head is None:
        return new_node
    if integer <= head.key:
        new_node.next = head
        return new_node
    curr = head
    while curr.next:
        curr_val = curr.key
        next_val = curr.next.key
        if integer >= curr_val and integer <= next_val:
            new_node.next = curr.next
            curr.next = new_node
            return head
        curr = curr.next  # 10->11->12->14->15->16->None
    if integer >= curr.key:
        curr.next = new_node
    return head

def print_middle_of_the_linked_list(head: ListNode):
    """Print middle element of the linked list"""

    # brute force
    """
    if head is None:
        return
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next

    element = (count-1)//2
    print(element)
    for _ in range(element):
        head = head.next
    return head.key
    """

    # efficient
    if head is None:
        return
    slow = head
    fast = head
    while fast!=None and fast.next!=None:
        slow = slow.next
        fast = fast.next.next

    return slow.key

def print_nth_node_from_last(head: ListNode, n: int):
    """Print nth node from the last"""

    # brute force
    # my approach
    """
    if head == None:
        return
    # get count
    count = 0
    curr = head
    while curr:
        curr = curr.next  # 10 12 13 14
        count += 1
    diff = count - n
    if diff < 0:
        return
    count = 0
    while head:
        if count == diff:
            return head.key
        count += 1
        head = head.next
    return
    """

    # efficient
    if head == None:
        return
    slow = head
    fast = head
    for _ in range(n):
        if fast == None:
            return
        fast = fast.next

    while fast != None:
        slow = slow.next
        fast = fast.next

    return slow.key

def remove_duplicate_element_from_sorted_linked_list(head: ListNode):
    """remove duplicate element from linked list"""
    # my approach
    # brute force
    if head == None:
        return None
    curr = head
    while curr != None and curr.next != None:
        if curr.key == curr.next.key:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

def reverse_a_linked_list(head: ListNode, prev=None):
    """reverse a given list"""

    # brute force
    """
    stack = []
    curr = head
    curr2 = head
    while curr:
        stack.append(curr.key)
        curr = curr.next
    while curr2:
        curr2.key = stack.pop()
        curr2 = curr2.next
    return head
    """

    # efficient
    """
    curr = head
    prev = None
    while curr != None:
        next = curr.next  # 10 15 20 25 30
        curr.next = prev
        prev = curr
        curr = next

    return prev
    """

    # recursive method 1
    """
    if head == None:
        return head
    if head.next == None:
        return head

    rest_head = reverse_a_linked_list(head.next)
    rest_tail = head.next
    rest_tail.next = head
    head.next = None
    return rest_head
    """

    # recursive method 2
    if head == None:
        return prev
    next = head.next
    head.next = prev
    return reverse_a_linked_list(next, head)



# search call
# print(search_item(15, head))

# insert at begin call
# head = insert_node_at_begin(3, head)

# head = insert_node_at_begin(4, head)

# head = insert_node_at_begin(5, head)

# insert at the end call
# head = insert_node_at_end(7, head)

# head = insert_node_at_end(11, head)

# head = insert_node_at_end(12, head)

# insert at given pos call
# head = insert_node_at_given_pos(14, 2, head)

# head = insert_node_at_given_pos(17, 6, head)

# head = insert_node_at_given_pos(18, 11, head)

# calls delete initial node
# head = delete_node_at_start(head)

# calls delete last node
# head = delete_last_node(head)

# calls delete node from middle with address given
# i = 0
# node = head
# while i != 1:
#     node = node.next
#     i+=1

# head = delete_node_from_middle_with_add(node, head)

# call insert element in sorted list (in sorted list)
# head1 = ListNode(5)
# head1.next = ListNode(10)
# head1.next.next = ListNode(15)
# head1.next.next.next = ListNode(20)
# head1.next.next.next.next = ListNode(25)

# head = insert_element_in_sorted_list(26, head1)

# call print middle element
# print(print_middle_of_the_linked_list(head))

# call print function for printing nth node from last
# print(print_nth_node_from_last(head, 1))

# call function that removes duplicate elements from linked list
# head = remove_duplicate_element_from_sorted_linked_list(head)

# call reverse a linked list function
head = reverse_a_linked_list(head)

printlist(head)
