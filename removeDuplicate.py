from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int | list[int]:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))