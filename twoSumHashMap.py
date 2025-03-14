from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if target - nums[i] in hm.keys() and i != hm[target - nums[i]]:
                return [i, hm[target - nums[i]]]
            hm[nums[i]] = i

        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
