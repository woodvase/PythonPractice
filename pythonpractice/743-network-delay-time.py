import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        dist[0] = 0
        dist[k] = 0
        pq = [(0, k)]
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        while len(pq) > 0:
            w, n = heapq.heappop(pq)
            for p in graph[n]:
                if dist[n] + p[0] < dist[p[1]]:
                    dist[p[1]] = dist[n] + p[0]
                    heapq.heappush(pq, (dist[p[1]], p[1]))
        ans = 0
        for d in dist:
            if d == float("inf"):
                return -1
            ans = max(ans, d)
        return ans


print(
    Solution().networkDelayTime(
        times=[
            [4, 2, 76],
            [1, 3, 79],
            [3, 1, 81],
            [4, 3, 30],
            [2, 1, 47],
            [1, 5, 61],
            [1, 4, 99],
            [3, 4, 68],
            [3, 5, 46],
            [4, 1, 6],
            [5, 4, 7],
            [5, 3, 44],
            [4, 5, 19],
            [2, 3, 13],
            [3, 2, 18],
            [1, 2, 0],
            [5, 1, 25],
            [2, 5, 58],
            [2, 4, 77],
            [5, 2, 74],
        ],
        n=5,
        k=3,
    )
)
