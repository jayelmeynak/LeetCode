import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left +=1
            right -=1
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))