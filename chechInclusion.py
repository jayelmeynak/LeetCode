class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, 0
        answer = False
        while left < len(s2):
            if s2[left] in s1:
                right = left
                cur_s1 = s1
                while right < len(s2) and right - left + 1 <= len(s1):
                    if s2[right] in cur_s1:
                        cur_s1 = cur_s1.replace(s2[right], '', 1)
                    if len(cur_s1) == 0:
                        return True
                    right += 1
            left += 1
        return answer

if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))
