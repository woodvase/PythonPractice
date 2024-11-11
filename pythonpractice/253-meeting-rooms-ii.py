from typing import List

"""

Code
Testcase
Test Result
Test Result
253. Meeting Rooms II
Medium
Topics
Companies
Hint
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sAndE = []
        for index, pair in enumerate(intervals):
            sAndE.append((pair[0], "start", index))
            sAndE.append((pair[1], "end", index))
        sortedStartEnd = sorted(sAndE, key=lambda x: (x[0], x[1]))
        maxOverlaps = 0
        counter = 0
        indexSet = set()
        overlappingIndexs = []
        for n in sortedStartEnd:
            if n[1] == "start":
                counter += 1
                indexSet.add(n[2])
                if counter > maxOverlaps:
                    maxOverlaps = counter
                    overlappingIndexs = list(indexSet)
            elif n[1] == "end":
                counter -= 1
                indexSet.discard(n[2])
        print(overlappingIndexs)
        return maxOverlaps


print(Solution().minMeetingRooms([[13, 15], [1, 13]]))
