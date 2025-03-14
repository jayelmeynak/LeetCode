from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        aim = len(nums) - 1
        for now in range(len(nums) - 1, -1, -1):
            if nums[now] + now >= aim:
                aim = now
        if aim == 0:
            return True
        return False

if __name__ == '__main__':
    print(Solution().canJump([3,2,1,0,4]))
