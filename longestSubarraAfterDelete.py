from typing import List


# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         if 0 not in nums:
#             return len(nums) - 1
#         max_len = 0
#         zero_index = 0
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 continue
#             start_index, right = i, i
#             count_zero = 0
#             while right < len(nums) and count_zero < 2:
#                 if nums[right] == 0:
#                     count_zero += 1
#                     if count_zero == 1:
#                         zero_index = right
#                 elif nums[right] == 1 and count_zero == 0:
#                     max_len = max(max_len, right - start_index + 1)
#                 elif nums[right] == 1 and count_zero == 1:
#                     max_len = max(max_len, right - start_index)
#                 right += 1
#             i = zero_index
#         return max_len

class Solution:
    def longestSubarray(selfself, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            if nums[i - 1] == 1:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if nums[i + 1] == 1:
                right[i] = right[i + 1] + 1
        max_len = 0
        for a, b in zip(left, right):
            max_len = max(max_len, a + b)
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.longestSubarray([1, 0, 1, 1, 0, 1, 1, 0, 1]))
# 0,1,1,1,0,1,1,0,1
# 0 1 2 3 4 5 6 7 8
