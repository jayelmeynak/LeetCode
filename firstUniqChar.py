class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for index, element in enumerate(s):
            if element in dic:
                dic[element][1] += 1
            else:
                dic[element] = [index, 1]
        for key, value in dic.items():
            if value[1] == 1:
                return value[0]
        return -1