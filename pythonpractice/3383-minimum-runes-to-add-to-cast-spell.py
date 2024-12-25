from collections import defaultdict, deque
from typing import Deque, List


# Strong connected components
class Solution:
    def minRunesToAdd(self, n: int, crystals: List[int], flowFrom: List[int], flowTo: List[int]) -> int:
        flowConnected = defaultdict(list)
        for i, f in enumerate(flowFrom):
            flowConnected[f].append(flowTo[i])

        q = deque(crystals)
        checked = set()
        while len(q) > 0:
            y = q.popleft()
            checked.add(y)
            for c in flowConnected[y]:
                if c not in checked:
                    q.append(c)
            flowConnected.pop(y, None)

        noSourceNodes = set([x for x in range(n)]) - checked

        stk = deque()

        def dfs(r, connected, shouldRecord):
            checked.add(r)
            for c in connected[r]:
                if c not in checked:
                    dfs(c, connected, shouldRecord)
            # make sure the source node is on the top of the stack
            if shouldRecord:
                stk.append(r)

        for uc in noSourceNodes:
            if uc not in checked:
                dfs(uc, flowConnected, True)

        checked.clear()
        cnt = 0
        while stk:
            a = stk.pop()
            if a not in checked:
                cnt += 1
                dfs(a, flowConnected, False)

        return cnt


class Solution1:
    def minRunesToAdd(self, n: int, crystals: List[int], flowFrom: List[int], flowTo: List[int]) -> int:
        def bfs(q: Deque[int]):
            while q:
                a = q.popleft()
                for b in g[a]:
                    if vis[b] == 1:
                        continue
                    vis[b] = 1
                    q.append(b)

        def dfs(a: int):
            vis[a] = 2
            for b in g[a]:
                if vis[b] > 0:
                    continue
                dfs(b)
            seq.append(a)

        g = [[] for _ in range(n)]
        for a, b in zip(flowFrom, flowTo):
            g[a].append(b)
        print(g)

        q = deque(crystals)
        vis = [0] * n
        for x in crystals:
            vis[x] = 1
        bfs(q)

        seq = []
        for i in range(n):
            if vis[i] == 0:
                dfs(i)
        seq.reverse()
        print(f"seq: {seq}")
        ans = 0
        for i in seq:
            if vis[i] == 2:
                q = deque([i])
                vis[i] = 1
                bfs(q)
                ans += 1
        return ans


s = Solution()
s1 = Solution1()
print("00000")
print(s.minRunesToAdd(n=5, crystals=[2], flowFrom=[4, 0, 1], flowTo=[1, 2, 2]))
print(s1.minRunesToAdd(n=5, crystals=[2], flowFrom=[4, 0, 1], flowTo=[1, 2, 2]))
print("11111")
print(s.minRunesToAdd(n=6, crystals=[0], flowFrom=[0, 1, 2, 3], flowTo=[1, 2, 3, 0]))
print(s1.minRunesToAdd(n=6, crystals=[0], flowFrom=[0, 1, 2, 3], flowTo=[1, 2, 3, 0]))
print("22222")
print(s.minRunesToAdd(n=7, crystals=[3, 5], flowFrom=[0, 1, 2, 3, 5], flowTo=[1, 2, 0, 4, 6]))
print(s1.minRunesToAdd(n=7, crystals=[3, 5], flowFrom=[0, 1, 2, 3, 5], flowTo=[1, 2, 0, 4, 6]))
print("33333")
print(s.minRunesToAdd(n=5, crystals=[4, 0, 3], flowFrom=[1, 4, 2, 1, 2], flowTo=[3, 3, 3, 4, 1]))
print(s1.minRunesToAdd(n=5, crystals=[4, 0, 3], flowFrom=[1, 4, 2, 1, 2], flowTo=[3, 3, 3, 4, 1]))
print("44444")
print(s.minRunesToAdd(n=5, crystals=[4, 2], flowFrom=[3, 1, 0], flowTo=[1, 4, 1]))
print(s1.minRunesToAdd(n=5, crystals=[4, 2], flowFrom=[3, 1, 0], flowTo=[1, 4, 1]))
print("55555")
print(s.minRunesToAdd(n=5, crystals=[0], flowFrom=[3, 1, 0, 4, 2, 4, 2, 0, 3], flowTo=[1, 0, 3, 0, 4, 1, 3, 1, 0]))
print(s1.minRunesToAdd(n=5, crystals=[0], flowFrom=[3, 1, 0, 4, 2, 4, 2, 0, 3], flowTo=[1, 0, 3, 0, 4, 1, 3, 1, 0]))
