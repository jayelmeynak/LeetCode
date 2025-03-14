
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False

        last = x % 10
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + last
            last = x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10

print(Solution().isPalindrome(313))  # Ожидается False

# class Solution2:
#     def isPalindrome(self, x: int) -> bool:
#         x_str = str(x)
#         return x_str == x_str[::-1]