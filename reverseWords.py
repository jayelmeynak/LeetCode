class Solution:

    def reverseWords(self, s):
        if not s or len(s) == 0:
            return s

        words = s.split(' ')
        reversed_words = [word[::-1] for word in words]
        return ' '.join(reversed_words)

    # def reverseWords(self, s: str) -> str:
    #     if not s or len(s) == 0:
    #         return s
    #     stop_index = 0
    #     left = right = 0
    #     s_new = ""
    #     while  right < len(s):
    #         if s[right] == ' ':
    #             left = right - 1
    #             while left != stop_index:
    #                 s_new += s[left]
    #                 left -= 1
    #             s_new += s[right]
    #             stop_index = right
    #         right += 1
    #     left = right - 1
    #     while left != stop_index:
    #         s_new += s[left]
    #         left -= 1
    #     s_new += s[stop_index]
    #     return s_new

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("Let's take LeetCode contest"))
