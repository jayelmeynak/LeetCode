from typing import List


class Solution:
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     res = []
    #     for i in range(len(nums1)):
    #         if nums1[i] in nums2:
    #             res.append(nums1[i])
    #             nums2.remove(nums1[i])
    #     return res

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dic1 = {}
        dic2 = {}
        for num1 in nums1:
            dic1[num1] = dic1.get(num1, 0) + 1
        for num2 in nums2:
            dic2[num2] = dic2.get(num2, 0) + 1
        for key in dic1.keys():
            repeat = min(dic1[key], dic2.get(key, 0))
            for i in range(repeat):
                res.append(key)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.intersect([2, 5], [1, 2, 2, 3, 4, 5]))
