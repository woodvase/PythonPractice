from typing import Optional

from binary_tree_node import TreeNode


class Solution:
    def has_node_1(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if root.val == 1:
            return True
        return self.has_node_1(root.left) or self.has_node_1(root.right)

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not self.has_node_1(root):
            return None
        root.left = self.pruneTree(root.left) if self.has_node_1(root.left) else None
        root.right = self.pruneTree(root.right) if self.has_node_1(root.right) else None

        if root.val == 0 and root.left is None and root.right is None:
            return None

        return root
