class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        def expand_around_center(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        start = end = 0
        for i in range(n):
            left1, right1 = expand_around_center(i, i)
            if right1 - left1 > end - start:
                start, end = left1, right1
            left2, right2 = expand_around_center(i, i + 1)
            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start: end + 1]

print(Solution().longestPalindrome("babaddaba"))