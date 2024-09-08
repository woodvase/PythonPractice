from typing import List, Optional

from binary_tree_node import TreeNode

"""
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Input: preorder = [1,3]
Output: [1,null,3]
"""


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder, 0, len(preorder) - 1)

    def helper(
        self, preorder: List[int], start: int, end: int
    ) -> Optional[TreeNode]:
        if start > end:
            return None
        root = TreeNode(preorder[start])
        rightTreeIndex = self.search(preorder, root.val, start, end)
        root.left = (
            self.helper(preorder, start + 1, rightTreeIndex - 1)
            if rightTreeIndex >= 0
            else self.helper(preorder, start + 1, end)
        )
        root.right = (
            self.helper(preorder, rightTreeIndex, end)
            if rightTreeIndex >= 0
            else None
        )
        return root

    def search(self, preorder: List[int], val: int, start: int, end: int):
        index = start
        while index <= end:
            if preorder[index] > val:
                return index
            index += 1

        return -1
