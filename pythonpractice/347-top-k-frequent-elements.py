from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        s = Counter(nums)
        sorted_by_frequency = sorted(
            s.items(), key=lambda x: x[1], reverse=True
        )
        return [x[0] for x in sorted_by_frequency[:k]]


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
