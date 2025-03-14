from typing import List


class Solution:
    def isReflection(self, points: List[List[int]]) -> bool:
        points_set = set()
        min_x = float("inf")
        max_x = float("-inf")
        for x, y in points:
            points_set.add((x, y))
            min_x = min(min_x, x)
            max_x = max(max_x, x)
        sum = min_x + max_x
        answer = True
        for x, y in points:
            if (sum - x, y) not in points_set:
                answer = False
                return answer
        return answer
