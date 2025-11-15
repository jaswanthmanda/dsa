class Node:
    def __init__(self, k):
        self.root = k
        self.left = None
        self.right = None


def postorder(root: Node):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.root)


# driver code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
postorder(root)

# output: 20 40 50 30 10
