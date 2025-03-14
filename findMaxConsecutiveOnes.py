from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = right = 0
        zero_counter = 1
        while right < len(nums):
            if nums[right] == 0:
                zero_counter -= 1
            if zero_counter < 0:
                if nums[left] == 0:
                    zero_counter += 1
                left += 1
            right += 1
        return right - left


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))