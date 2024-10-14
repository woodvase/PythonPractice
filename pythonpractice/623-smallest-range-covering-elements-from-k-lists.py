import heapq
from collections import defaultdict
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        # Heap sort all the numbers with the list position infomation.
        # the list position infomation is used to ensure the range has at least one element for all the lists
        for listPosition, numList in enumerate(nums):
            for n in numList:
                heapq.heappush(pq, (n, listPosition))
        sorted = []
        while pq:
            sorted.append(heapq.heappop(pq))

        # Now we need to get the minimim range to have at least one element of all the lists
        # To ensure we have at least one element of all the lists, we use a dictionary to record how many elements contained in the sliding window
        dict = defaultdict(int)
        start = 0
        ans = [sorted[0][0], sorted[len(sorted) - 1][0]]
        for index, pair in enumerate(sorted):
            # add an element to the sliding window
            dict[pair[1]] += 1
            if self.hasAll(dict, nums):
                # try to shorten the sliding window to get the min range
                while dict[sorted[start][1]] > 1:
                    dict[sorted[start][1]] -= 1
                    start += 1

                newR = [sorted[start][0], sorted[index][0]]
                diff = ans[1] - ans[0]
                diffR = newR[1] - newR[0]
                if diffR < diff or (diffR == diff and newR[0] < ans[0]):
                    ans = newR
                # since we will add new element to the sliding window, remove the first one
                dict[sorted[start][1]] -= 1
                start += 1
        return ans

    def hasAll(self, dict, nums):
        if len(dict) < len(nums):
            return False
        for v in dict.values():
            if v < 1:
                return False
        return True


print(
    Solution().smallestRange(
        [
            [11, 38, 83, 84, 84, 85, 88, 89, 89, 92],
            [28, 61, 89],
            [52, 77, 79, 80, 81],
            [21, 25, 26, 26, 26, 27],
            [9, 83, 85, 90],
            [84, 85, 87],
            [26, 68, 70, 71],
            [36, 40, 41, 42, 45],
            [-34, 21],
            [-28, -28, -23, 1, 13, 21, 28, 37, 37, 38],
            [-74, 1, 2, 22, 33, 35, 43, 45],
            [54, 96, 98, 98, 99],
            [43, 54, 60, 65, 71, 75],
            [43, 46],
            [50, 50, 58, 67, 69],
            [7, 14, 15],
            [78, 80, 89, 89, 90],
            [35, 47, 63, 69, 77, 92, 94],
        ]
    )
)
