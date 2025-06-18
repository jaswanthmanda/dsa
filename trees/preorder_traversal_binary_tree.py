class Node:
    def __init__(self, k):
        self.left = None
        self.right = None
        self.k = k


def preorder(root: Node):
    if root is not None:
        print(root.k, end=" ")
        preorder(root.left)
        preorder(root.right)


# Driver code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
preorder(root)

# TC: O(n)
# SC: O(h)
