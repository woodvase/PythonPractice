from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        sortedTickets = sorted(tickets, key=lambda x: x[1])
        startToEndMap = dict()
        for t in sortedTickets:
            if t[0] in startToEndMap:
                startToEndMap[t[0]].append(t[1])
            else:
                startToEndMap[t[0]] = [t[1]]
        print(startToEndMap)
        ans = []
        self.dfs(startToEndMap, "JFK", ans)

        return ans[::-1]

    def dfs(self, ticketsMap, start, result):
        # if depart city has flight and the flight can go to another city
        while start in ticketsMap and len(ticketsMap[start]) > 0:
            # 找到s能到哪里，选能到的第一个机场
            v = ticketsMap[start][0]  # we go to the 1 choice of the city
            # 在之后的可选项机场中去掉这个机场
            ticketsMap[start].pop(0)  # get rid of this choice since we used it
            # 从当前的新出发点开始
            self.dfs(ticketsMap, v, result)  # we start from the new airport

        result.append(
            start
        )  # after append, it will back track to last node, thus the result list is in reversed order


print(
    Solution().findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]])
)
