from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        r = 0
        for n1 in arr1:
            for n2 in arr2:
                c = self.lengthCommonPrefix(n1, n2)
                r = max(r, c)
        return r

    def lengthCommonPrefix(self, arr1: int, arr2: int) -> int:
        str1 = str(arr1)
        str2 = str(arr2)
        i1 = 0
        i2 = 0
        while i1 < len(str1) and i2 < len(str2) and str1[i1] == str2[i2]:
            i1 += 1
            i2 += 1
        return i1


class Solution1:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        allPrefixes = set()
        for n in arr1:
            while n > 0:
                allPrefixes.add(n)
                n = n // 10

        r = 0
        for n in arr2:
            while n > 0:
                if n in allPrefixes:
                    r = max(r, len(str(n)))
                else:
                    n = n // 10
        return r
