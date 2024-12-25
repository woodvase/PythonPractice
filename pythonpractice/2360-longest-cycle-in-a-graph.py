from collections import defaultdict, deque
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)

        inDegrees = [0] * n
        for e in edges:
            if e != -1:
                inDegrees[e] += 1
        q = deque()
        for i in range(n):
            if inDegrees[i] == 0:
                q.append(i)
        out = set()
        while len(q):
            i = q.popleft()
            out.add(i)
            neighbor = edges[i]
            if neighbor != -1:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    q.append(neighbor)

        if len(out) == n:
            return -1

        incycles = [x for x in range(n) if x not in out]
        cycleLen = defaultdict(int)
        visisted = set()

        def dfs(n, li):
            if n in visisted:
                return
            visisted.add(n)
            cycleLen[li] += 1
            dfs(edges[n], li)

        for i in incycles:
            if i not in visisted:
                dfs(i, i)
        max = 0
        for c in cycleLen.values():
            if c > max:
                max = c
        return max


s = Solution()
print(s.longestCycle([3, 3, 4, 2, 3]))
print(s.longestCycle([2, -1, 3, 1]))
