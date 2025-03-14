from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (nums[mid] == target):
                return mid
            if (nums[left] < nums[mid]):
                if (nums[left] <= target <= nums[mid]):
                    right = mid
                else:
                    left = mid + 1
            else:
                if (nums[mid] <= target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid
        if (nums[left] == target):
            return left
        else: return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[0] <= nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[n - 1]:
                    left = mid + 1
                else:
                    right = mid
        return left if nums[left] == target else -1

if __name__ == '__main__':
    s = Solution()
    print(s.search([3,1], 1))
