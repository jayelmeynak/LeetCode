from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for interval in intervals:
            if len(ans) == 0:
                ans.append(interval)
            elif interval[0] <= ans[-1][1]:
                ans[-1][1] = max(interval[1], ans[-1][1])
            else:
                ans.append(interval)
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))

