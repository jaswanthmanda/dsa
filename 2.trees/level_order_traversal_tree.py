class Node:
    def __init__(self, k):
        self.k = k
        self.right = None
        self.left = None


def height(root: Node):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1


def printKdist(root: Node, k: int):
    if root is None:
        return
    if k == 0:
        print(root.k, end=" ")
    else:
        printKdist(root.left, k - 1)
        printKdist(root.right, k - 1)


# driver code
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)


height_of_tree = height(root)

for i in range(height_of_tree):
    printKdist(root, i)
    print()
