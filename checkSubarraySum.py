from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        if sum(nums) % k == 0 and len(nums) != 1:
            return True
        dic = {}
        cur_mod = 0
        for i, num in enumerate(nums):
            cur_mod = (cur_mod + num) % k
            if cur_mod == 0 and i != 0:
                return True
            if cur_mod in dic and i - dic[cur_mod] > 1:
                return True
            if cur_mod not in dic:
                dic[cur_mod] = i
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkSubarraySum([1,0], 2))
