# Closed binary search
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, node, target):
        if node is None:
            return

        if abs(node.val - target) < abs(self.close - target):
            self.close = node.val

        if abs(node.val - target) == abs(self.close - target) and node.val < self.close:
            self.close = node.val

        if target > node.val:
            self.helper(node.right, target)
        else:
            self.helper(node.left, target)

    def closestValue(
        self,
        root: Optional[TreeNode],
        target: float,
    ) -> int:
        # base case
        if root is None:
            return None

        self.close = root.val

        self.helper(root, target)

        return self.close