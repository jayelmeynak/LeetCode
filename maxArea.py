from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            now_area = (r - l) * min(height[l], height[r])
            max_area = max(now_area, max_area)
            if height[l] < height[r]:
                l += 1
                continue
            if height[l] >= height[r]:
                r -= 1
                continue
        return max_area

if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))