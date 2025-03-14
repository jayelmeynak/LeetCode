class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dic1[s[i]] = dic1.get(s[i], 0) + 1
            dic2[t[i]] = dic2.get(t[i], 0) + 1
        for key, value in dic1.items():
            value2 = dic2.get(key, 0)
            if value != value2:
                return False
        return True

