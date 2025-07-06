import math


class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None


def max_val_in_tree(root: Node):

    if root is None:
        return -1 * math.inf
    else:
        max_val_left = max_val_in_tree(root.left)
        max_val_right = max_val_in_tree(root.right)
        return max(
            max_val_left,
            max_val_right,
            root.k,
        )


# driver code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

max_val = max_val_in_tree(root)

print(max_val)
