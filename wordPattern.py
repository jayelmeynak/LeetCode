class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s2 = s.split()
        if len(pattern) != len(s2):
            return False
        dic, dic2 = {}, {}
        for sc, tc in zip(pattern, s2):
            if (sc in dic and dic[sc] != tc) or (tc in dic2 and dic2[tc] != sc):
                return False
            dic[sc] = tc
            dic2[tc] = sc
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat dog"))