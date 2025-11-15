from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def level_order_traversal_print(root: Node):
    