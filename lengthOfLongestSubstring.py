class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        symbols = dict()
        l = r = best_l = best_r = 0
        while r < len(s):
            symbols[s[r]] = symbols.get(s[r], 0) + 1
            if symbols.get(s[r], 0) < 2:
                if r - l > best_r - best_l:
                    best_r, best_l = r, l
            else:
                while symbols.get(s[r], 0) >= 2:
                    symbols[s[l]] = symbols.get(s[l]) - 1
                    l += 1
            r += 1
        return best_r - best_l + 1

print(Solution().lengthOfLongestSubstring("abcabcbb"))