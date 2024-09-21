from typing import List, Optional

from binary_tree_node import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        stk = [root]
        while len(stk) > 0:
            node = stk.pop()
            ans.append(node.val)
            if node.right is not None:
                stk.append(node.right)
            if node.left is not None:
                stk.append(node.left)
        return ans
