from typing import Deque, List, Optional

from binary_tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = Deque([root])
        while len(q) > 0:
            l = []
            s = len(q)
            while s > 0:
                n = q.popleft()
                l.append(n.val)
                s -= 1
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            ans.append(l)
        return ans
