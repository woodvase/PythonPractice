class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for c in s:
            if len(stk) == 0 or c != stk[len(stk) - 1]:
                stk.append(c)
            else:
                if c == stk[len(stk) - 1]:
                    stk.pop()
        return "".join(stk)


print(Solution().removeDuplicates("azxxzy"))
