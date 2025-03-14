from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        new_list = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if (nums[left] ** 2 >= nums[right] ** 2):
                new_list[i] = nums[left] ** 2
                left += 1
            else:
                new_list[i] = nums[right] ** 2
                right -= 1
        return new_list


if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
