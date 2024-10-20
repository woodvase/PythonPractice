from collections import Counter
from typing import List

"""
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        if not len(people):
            return ans

        weightCnt = Counter(people)
        weights = sorted(weightCnt.keys(), key=lambda x: x, reverse=True)

        start = 0
        end = len(weights) - 1
        while start <= end:
            sw = weights[start]
            ew = weights[end]

            if start == end:
                if limit >= 2 * sw:
                    a, b = divmod(weightCnt[sw], 2)
                    ans += a + b
                else:
                    ans += weightCnt[sw]
                return ans

            diff = limit - sw
            if ew <= diff:
                n = min(weightCnt[sw], weightCnt[ew])
                ans += n
                weightCnt[sw] -= n
                weightCnt[ew] -= n
                if weightCnt[sw] == 0:
                    start += 1
                if weightCnt[ew] == 0:
                    end -= 1
            else:
                ans += weightCnt[sw]
                start += 1
        return ans


print(Solution().numRescueBoats([3, 5, 3, 4], 5))
