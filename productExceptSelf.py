from typing import List

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer = []
#         for i in range(len(nums)):
#             ans = 1
#             left, right = i - 1, i + 1
#             while left >= 0 or right < len(nums):
#                 if (left >= 0):
#                     ans *= nums[left]
#                     left -= 1
#                 if (right < len(nums)):
#                     ans *= nums[right]
#                     right += 1
#             answer.append(ans)
#         return answer

"""
Спизженное решение с ютуба https://www.youtube.com/watch?v=yKZFurr4GQA
"""


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         l_mult = 1
#         r_mult = 1
#         n = len(nums)
#         l_arr = [0] * n
#         r_arr = [0] * n
#         for i in range(n):
#             j = -i - 1
#             l_arr[i] = l_mult
#             r_arr[j] = r_mult
#             l_mult *= nums[i]
#             r_mult *= nums[j]
#         for i in range(n):
#             answer = l_arr[i] * r_arr[i]
#         return [l * r for l, r in zip(l_arr, r_arr)]


class Solution:
    def prefixMult(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i in range(1, len(nums)):
            ans.append(ans[i - 1] * nums[i - 1])
        return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []
        nums_mult = self.prefixMult(nums)
        nums_mult_inverse = self.prefixMult(nums[::-1])[::-1]
        for i in range(n):
            answer.append(nums_mult[i] * nums_mult_inverse[i])
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
