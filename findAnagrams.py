from typing import List


class Solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     p1 = sorted(p)
    #     ans = []
    #     left, right = 0, len(p) - 1
    #     while right < len(s):
    #         subString = s[left:right+1]
    #         if sorted(subString) == p1:
    #             ans.append(left)
    #         left += 1
    #         right += 1
    #     return ans
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pHashMap = {}
        sHashMap = {}
        ans = []
        for i in range(len(p)):
            pHashMap[p[i]] = pHashMap.get(p[i], 0) + 1
        left, right = 0, 0
        while right < len(s):
            sHashMap[s[right]] = sHashMap.get(s[right], 0) + 1
            if sHashMap == pHashMap:
                ans.append(left)
            right += 1
            if right - left == len(p):
                sHashMap[s[left]] = sHashMap.get(s[left], 0) - 1
                if sHashMap[s[left]] == 0:
                    del sHashMap[s[left]]
                left += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams(s="cbaebabacd", p="abc"))
