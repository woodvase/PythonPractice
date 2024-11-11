from typing import List

from DisjointSet import DisjointSet


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return []
        djs = DisjointSet(len(edges))
        ans = []
        for node1, node2 in edges:
            if djs.find(node1) == djs.find(node2):
                ans = [node1, node2]
            else:
                djs.union(node1, node2)
        return ans


print(
    Solution().findRedundantConnection(
        [
            [9, 10],
            [5, 8],
            [2, 6],
            [1, 5],
            [3, 8],
            [4, 9],
            [8, 10],
            [4, 10],
            [6, 8],
            [7, 9],
        ]
    )
)
