# Flatten a binary tree to linked list
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preorder(node):
            if not node:
                return node

            left_tail = preorder(node.left)
            right_tail = preorder(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            return right_tail or left_tail or node

        preorder(root)
