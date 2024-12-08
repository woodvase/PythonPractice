import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buyBacklog = []
        sellBacklog = []
        for o in orders:
            orderType = o[2]
            # 0 for buy and 1 for sell
            if orderType == 1:
                remained = o[1]
                while remained > 0 and len(buyBacklog) > 0 and -buyBacklog[0][0] >= o[0]:
                    remained = remained - buyBacklog[0][1]
                    if remained >= 0:
                        heapq.heappop(buyBacklog)
                    else:
                        s = heapq.heappop(buyBacklog)
                        heapq.heappush(buyBacklog, (s[0], -remained))
                if remained > 0:
                    heapq.heappush(sellBacklog, (o[0], remained))
            elif orderType == 0:
                remained = o[1]
                while remained > 0 and len(sellBacklog) > 0 and sellBacklog[0][0] <= o[0]:
                    remained = remained - sellBacklog[0][1]
                    if remained >= 0:
                        heapq.heappop(sellBacklog)
                    else:
                        s = heapq.heappop(sellBacklog)
                        heapq.heappush(sellBacklog, (s[0], -remained))
                if remained > 0:
                    heapq.heappush(buyBacklog, (-o[0], remained))
        buyCnt = sum([x[1] for x in buyBacklog])
        sellCnt = sum([x[1] for x in sellBacklog])
        return (buyCnt + sellCnt) % (10**9 + 7)


s = Solution()
print(s.getNumberOfBacklogOrders([[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]))
