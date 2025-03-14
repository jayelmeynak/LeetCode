from typing import List


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         candidate = None
#         count = 0
#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)
#         return candidate


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        max_num = 0
        max_count = 0
        for num in dic:
            if dic[num] > max_count:
                max_count = dic[num]
                max_num = num
        return max_num

if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([2, 1, 2, 1, 2, 1, 2, 1, 2, 1]))
