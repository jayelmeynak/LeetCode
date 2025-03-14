from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = right = 0
        while seats[left] != 1:
            left += 1
        max_length = left - 0 if left != 0 else 0

        right = left + 1

        while right < len(seats):
            if seats[right] == 1:
                lenght = right - left
                position = left + lenght // 2
                max_length = max(max_length, position - left)
                left = right
            right += 1

        if seats[right - 1] != 1:
            max_length = max(max_length, right - 1 - left)
        return max_length

