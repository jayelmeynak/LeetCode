from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        smallest, end, far = 0, 0, 0
        n = len(nums)
        for i in range(n - 1):
            far = max(far, i + nums[i])
            if (i == end):
                smallest += 1
                end = far
        return smallest

if __name__ == '__main__':
    s = Solution()
    print(s.jump([2,3,1,1,4]))
