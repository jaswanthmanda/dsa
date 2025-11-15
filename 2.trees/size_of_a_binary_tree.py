class Node:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None


def size_of_a_binary_tree(root: Node):
    if root is None:
        return 0
    else:
        return size_of_a_binary_tree(root.left) + size_of_a_binary_tree(root.right) + 1


# driver code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
size = size_of_a_binary_tree(root)
print("Size of binary tree: ", size)
