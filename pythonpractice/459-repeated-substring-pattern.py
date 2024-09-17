class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        i = 0
        while i < l:
            left = s[: l - i - 1]
            right = s[i + 1 :]
            if left == right:
                return True
            i += 1
        return False
