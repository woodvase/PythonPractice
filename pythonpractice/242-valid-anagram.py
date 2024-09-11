class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for c in s:
            if c not in dict:
                dict[c] = 0
            else:
                dict[c] = dict[c] + 1
        for c in t:
            if c not in dict:
                return False
            dict[c] = dict[c] - 1
        return len([k for k, v in dict.items() if v != 0]) == 0


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = [0 for i in range(26)]
        for c in s:
            dict[ord(c) - ord("a")] += 1
        for c in t:
            dict[ord(c) - ord("a")] -= 1
        return len([c for c in dict if c != 0]) == 0
