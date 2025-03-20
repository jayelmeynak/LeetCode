from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        arr = []
        left = right = 0
        while left < n and right < m:
            if nums1[left] < nums2[right]:
                arr.append(nums1[left])
                left += 1
            else:
                arr.append(nums2[right])
                right += 1
        while left < n:
            arr.append(nums1[left])
            left += 1
        while right < m:
            arr.append(nums2[right])
            right += 1
        z = len(arr)
        mid = z // 2
        ans = 0
        if z % 2 == 0:
            ans = (arr[mid] + arr[mid - 1]) / 2
        else:
            ans = arr[mid]
        return ans
