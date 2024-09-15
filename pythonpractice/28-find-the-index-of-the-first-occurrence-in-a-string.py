class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = -1
        next = self.findCommonStr(needle)
        print(next)
        for j, c in enumerate(haystack):
            while i >= 0 and c != needle[i + 1]:
                i = next[i]
            if c == needle[i + 1]:
                i += 1
            if i == len(needle) - 1:
                return j - len(needle) + 1

        return -1

    def findCommonStr(self, needle: str) -> list:
        next = [-1] * len(needle)
        i = -1
        j = 1
        while j < len(needle):
            while i >= 0 and needle[j] != needle[i + 1]:
                i = next[i]

            if needle[j] == needle[i + 1]:
                i += 1
            next[j] = i
            j += 1
        return next


s = Solution()
print(s.strStr("aacaasaab", "aab"))
