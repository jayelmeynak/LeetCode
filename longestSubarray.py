from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        if 1 not in nums:
            return 0
        if nums.count(1) == 1:
            return 1
        res_left = [0] * len(nums)
        res_right = [0] * len(nums)
        for i in range(1,len(nums)):
            if nums[i-1] == 1:
                res_left[i] =  res_left[i-1] + 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i+1] == 1:
                res_right[i] = res_right[i+1] + 1
        res = 0
        for i in range(len(nums)):
            if res_left[i] + res_right[i]>res:
                res = res_left[i] + res_right[i]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.longestSubarray([1,1,1,0]))


#[4, 9] len 15
# [1, 0, 1, 1] len = 15
# [0, 0, 0]
# [4, 9, 14] len = 15
# [4, 9, 14, 19] len = 20
