from collections import defaultdict


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mappings = defaultdict(str)
        for s in key:
            if s not in mappings and s != " ":
                mappings[s] = chr(ord("a") + len(mappings))
        ans = ""
        for s in message:
            if s != " ":
                ans += mappings[s]
            else:
                ans += s
        return ans


s = Solution()
print(s.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
