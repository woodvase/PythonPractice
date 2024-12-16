# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from pythonpractice.binary_tree_node import TreeNode


# Time memory exceeded
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth = self.maxDepth(root)
        if depth == 0 or depth == 1:
            return depth
        level = 1
        q = [root]
        w = 1
        while level <= depth:
            j = len(q) - 1
            while j >= 0 and not q[j]:
                j -= 1
            i = 0
            while i <= j and not q[i]:
                i += 1

            w = max(w, j - i + 1)
            levelNodes = q[i : j + 1]
            q.clear()
            for node in levelNodes:
                if node:
                    q.append(node.left)
                    q.append(node.right)
                else:
                    q.append(None)
                    q.append(None)
            level += 1
        return w

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution1:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        w = 1
        q = [(root, 0)]
        while len(q):
            _, start_index = q[0]
            for n in range(len(q)):
                node, _index = q.pop(0)
                if node.left:
                    q.append((node.left, 2 * _index + 1))
                if node.right:
                    q.append((node.right, 2 * _index + 2))
            w = max(w, _index - start_index + 1)
        return w
