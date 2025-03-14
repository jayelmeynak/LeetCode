class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return self.isOneEditDistance(t, s)
        len_s = len(s)
        len_t = len(t)
        if len_s - len_t > 1:
            return False
        for i in range(len_t):
            if s[i] != t[i]:
                if len_s == len_t:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i + 1:] == t[i:]

        return len_s == len_t + 1
