from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        answer = len(points)
        prev = points[0]
        for i in range(1, len(points)):
            curr = points[i]
            if curr[0] <= prev[1]:
                answer -= 1
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                prev = curr
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.findMinArrowShots([[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]))
