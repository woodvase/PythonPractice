import heapq
from bisect import bisect_right
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dict:
            v = self.dict[key]
            i = bisect_right(v, timestamp, key=lambda x: x[0])
            if i > 0 and i <= len(v):
                return v[i - 1][1]
            else:
                return ""
        else:
            return ""


timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
# store the key "foo" and value "bar" along with timestamp = 1.
timeMap.set("foo", "bar", 2)
# store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 3))
# return "bar"
timeMap.get("foo", 3)
# return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4)
# store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4)
# return "bar2"
timeMap.get("foo", 5)
# return "bar2"
