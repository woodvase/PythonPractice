import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter

        s = Counter(words)
        sortByFrequency = sorted(s, key=lambda x: (-s[x], x))
        return sortByFrequency[:k]
