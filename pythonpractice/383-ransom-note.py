class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        dict1 = Counter(ransomNote)
        dict2 = Counter(magazine)
        for k, v in dict1.items():
            if k not in dict2 or dict2[k] < v:
                return False
        return True