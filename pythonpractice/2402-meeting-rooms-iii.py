import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        roomUsage = [0] * n
        sortedMeetings = sorted(meetings, key=lambda x: x[0])
        pqRoomFree = []
        pqRoomInUse = []
        for x in range(n):
            heapq.heappush(pqRoomFree, x)

        for index, meeting in enumerate(sortedMeetings):
            while len(pqRoomInUse) > 0 and pqRoomInUse[0][0] <= meeting[0]:
                endedRoom = heapq.heappop(pqRoomInUse)[1]
                heapq.heappush(pqRoomFree, endedRoom)

            if len(pqRoomFree) > 0:
                room = heapq.heappop(pqRoomFree)
                roomUsage[room] += 1
                heapq.heappush(pqRoomInUse, (meeting[1], room))
            else:
                endTime, roomNum = heapq.heappop(pqRoomInUse)
                roomUsage[roomNum] += 1
                newEndTime = meeting[1] + endTime - meeting[0]
                heapq.heappush(pqRoomInUse, (newEndTime, roomNum))
        maxUsed = 0
        ans = 0
        print(roomUsage)
        for index, x in enumerate(roomUsage):
            if x > maxUsed:
                ans = index
                maxUsed = x
        return ans


print(Solution().mostBooked(2, [[0, 10], [1, 2], [12, 14], [13, 15]]))
