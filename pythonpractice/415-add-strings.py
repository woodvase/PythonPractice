"""
Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            return self.addStrings(num2, num1)

        l1 = len(num1)
        if l1 == 0:
            return num2

        ans = ""
        flag = 0
        l2 = len(num2)
        subNum2 = num2[l2 - l1 :]
        restNum2 = num2[: l2 - l1]

        while l1 > 0:
            n1 = int(num1[l1 - 1])
            n2 = int(subNum2[l1 - 1])
            a, b = divmod(n1 + n2 + flag, 10)
            flag = a
            ans = str(b) + ans
            l1 -= 1

        if not flag:
            return restNum2 + ans
        return self.addStrings(str(flag), restNum2) + ans


print(Solution().addStrings("999", "1"))
