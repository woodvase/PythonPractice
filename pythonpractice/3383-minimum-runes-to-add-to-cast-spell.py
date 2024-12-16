from collections import defaultdict, deque
from typing import List


class Solution:
    def minRunesToAdd(self, n: int, crystals: List[int], flowFrom: List[int], flowTo: List[int]) -> int:
        connected = defaultdict(list)
        for i, f in enumerate(flowFrom):
            connected[f].append(flowTo[i])
        q = deque(crystals)
        checked = set()
        while len(q) > 0:
            y = q.popleft()
            checked.add(y)
            for c in connected[y]:
                if c not in checked:
                    q.append(c)
            connected.pop(y, None)

        print(checked)
        def dfs(r, connected):
            if r not in checked:
                checked.add(r)
                for c in connected[r]:
                    dfs(c, connected)

        treeCnt = 0
        unconnected = set([x for x in range(n)]) - checked
        print(unconnected)
        print(connected)
        checked.clear()
        for r in unconnected:
            if len(connected[r]) > 0 and r not in checked:
                treeCnt += 1
                dfs(r, connected)
        print(checked)
        remained = [x for x in unconnected if x not in checked]
        return treeCnt + len(remained)


s = Solution()
print(s.minRunesToAdd(n=5, crystals=[2], flowFrom=[4, 0, 1], flowTo=[1, 2, 2]))
#print(s.minRunesToAdd(n=6, crystals=[0], flowFrom=[0, 1, 2, 3], flowTo=[1, 2, 3, 0]))
#print(s.minRunesToAdd(n=7, crystals=[3, 5], flowFrom=[0, 1, 2, 3, 5], flowTo=[1, 2, 0, 4, 6]))
#print(s.minRunesToAdd(n=3, crystals=[2], flowFrom=[1, 1], flowTo=[0, 2]))
