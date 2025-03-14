from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.append(nums1[i])
                nums2.remove(nums1[i])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intersect([2, 5], [1, 2, 2, 3, 4, 5]))
