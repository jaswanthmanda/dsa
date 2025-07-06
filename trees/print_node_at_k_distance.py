class Node:
    def __init__(self, k):
        self.k = k
        self.right = None
        self.left = None


def printKDist(root: Node, k: int):
    if root is None:
        return
    if k == 0:
        print(root.k, end=" ")
    else:
        printKDist(root.left, k - 1)
        printKDist(root.right, k - 1)


# driver code
root = Node(10)
root.right = Node(20)
root.left = Node(30)
root.left.right = Node(40)
root.left.left = Node(50)
printKDist(root, 2)
