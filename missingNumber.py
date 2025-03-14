from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic = {i: 0 for i in range(len(nums) + 1)}
        for i in nums:
            dic[i] += 1
        for key in dic.keys():
            if dic[key] != 1:
                return key

if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3,0,1]))