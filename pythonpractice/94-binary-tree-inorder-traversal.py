from typing import List, Optional

from binary_tree_node import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        stk = [root]
        n = root
        while len(stk) > 0:
            while n and n.left:
                stk.append(n.left)
                n = n.left
            if len(stk) > 0:
                n = stk.pop()
                ans.append(n.val)
                n = n.right
                if n:
                    stk.append(n)
        return ans
