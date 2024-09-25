from typing import List


class DisjoinSet:
    def __init__(self) -> None:
        self.parents = dict()
        self.sizes = dict()

    def find(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.sizes[x] = 1
            return x
        else:
            if x == self.parents[x]:
                return x
            else:
                return self.find(self.parents[x])

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.sizes[px] >= self.sizes[py]:
            self.parents[py] = px
            self.sizes[px] += self.sizes[py]
        else:
            self.parents[px] = py
            self.sizes[py] += self.sizes[px]

    def get_cluster(self):
        c = {}
        for k, v in self.parents.items():
            root = self.find(v)
            if root not in c:
                c[root] = [k]
            else:
                c[root].append(k)
        return c


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        aux = set(nums)
        ans = 0
        ds = DisjoinSet()
        for x in aux:
            ds.find(x)
            if x + 1 in ds.parents:
                ds.union(x, x + 1)
            if x - 1 in ds.parents:
                ds.union(x - 1, x)
        for s in ds.sizes:
            ans = max(ans, ds.sizes[s])

        print(ds.get_cluster())
        return ans


print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
