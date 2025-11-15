class Node:
    def __init__(self, k):
        self.root = k
        self.left = None
        self.right = None


def height(root: Node):
    if root is None:
        return 0
    else:
        lh = height(root.left)
        rh = height(root.right)
        return max(lh, rh) + 1


# driver code
# driver code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
height_val = height(root=root)
print(height_val)
