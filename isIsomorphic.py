class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic, dic2 = {}, {}
        for sc, tc in zip(s, t):
            if (sc in dic and dic[sc] != tc) or (tc in dic2 and dic2[tc] != sc):
                return False
            dic[sc] = tc
            dic2[tc] = sc
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic("badc", "baba"))