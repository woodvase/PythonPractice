from collections import defaultdict, deque
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)

        inDegrees = defaultdict(set)
        for i, node in enumerate(edges):
            if node > -1:
                inDegrees[node].add(i)
        q = deque()
        for i in range(n):
            if len(inDegrees[i]) == 0:
                q.append(i)
        out = set()
        while len(q):
            i = q.popleft()
            out.add(i)
            neighbor = edges[i]
            if neighbor != -1:
                v = inDegrees[neighbor]
                v.remove(i)
                if len(v) == 0:
                    q.append(neighbor)
        if len(out) == n:
            return -1

        incycles = set(range(n)) - out
        cycleLen = defaultdict(int)
        visisted = set()

        def dfs(n, inDegrees, li):
            if n in visisted:
                return
            visisted.add(n)
            cycleLen[li] += 1
            for x in inDegrees[n]:
                dfs(x, inDegrees, li)

        for i in incycles:
            if i not in visisted:
                dfs(i, inDegrees, i)
        max = 0
        for c in cycleLen.values():
            if c > max:
                max = c
        return max
