class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0 and len(s) == 0:
            return True
        if len(t) == 0 and len(s) != 0:
            return False
        i, j = 0, 0
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                if i == len(s):
                    return True
            j += 1
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isSubsequence("abc", "ahbgdc"))
