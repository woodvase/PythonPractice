"""
Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
"""


class Solution:
    def partitionString(self, s: str) -> int:
        p = 0
        if len(s) == 0:
            return p
        sub_set = set()
        for char in s:
            if char in sub_set:
                p += 1
                sub_set.clear()
            sub_set.add(char)

        return p + 1
