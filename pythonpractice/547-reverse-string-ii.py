class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        l = len(s)
        n = l // k
        for i in range(0, n + 1):
            if i % 2 == 0:
                tmp = ""
                start = k * i
                end = min(start + k - 1, l - 1)
                while start <= end:
                    tmp += s[end]
                    end -= 1
                ans += tmp
            else:
                ans += s[k * i : k * i + k]
        return ans


s = Solution()
print(s.reverseStr("abcdef123", 3))
