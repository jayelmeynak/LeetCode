from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        maxpos = 0
        for i in range(len(height)):
            if height[i] > height[maxpos]:
                maxpos = i
        ans = 0
        nowMax = 0
        for i in range(maxpos):
            if nowMax > height[i]:
                ans += (nowMax - height[i])
            if nowMax < height[i]:
                nowMax = height[i]
        nowMax = 0
        for i in range(len(height) - 1, maxpos, -1):
            if nowMax > height[i]:
                ans += (nowMax - height[i])
            if nowMax < height[i]:
                nowMax = height[i]
        return ans
