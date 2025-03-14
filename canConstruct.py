class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        dic = {}
        for i in range(len(ransomNote)):
            dic[ransomNote[i]] = dic.get(ransomNote[i], 0) + 1
        for i in range(len(magazine)):
            if magazine[i] in dic and dic[magazine[i]] > 0:
                dic[magazine[i]] -= 1
        for i in dic.keys():
            if dic[i] > 0:
                return False
        return True