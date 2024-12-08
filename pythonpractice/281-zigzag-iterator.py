from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.indexes = [0, 0]
        self.lists = [v1, v2]
        self.len = len(v1) + len(v2)

    def next(self) -> int:
        cur = sum(self.indexes)
        if cur < 2 * min(len(self.lists[0]), len(self.lists[1])):
            f = cur % 2
            v = self.lists[f][self.indexes[f]]
            self.indexes[f] += 1
            return v
        else:
            f = 0
            if self.indexes[f] >= len(self.lists[f]):
                f = 1
            v = self.lists[f][self.indexes[f]]
            self.indexes[f] += 1
            return v

    def hasNext(self) -> bool:
        return sum(self.indexes) < self.len
