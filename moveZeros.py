from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = r = 0
        while l < len(nums) and nums[l] != 0:
            l += 1
        r = l + 1
        while r < len(nums):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
            r += 1
        while l < len(nums):
            nums[l] = 0
            l += 1

if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))
