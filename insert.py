from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        for interval in intervals:
            if len(ans) == 0:
                ans.append(interval)
            elif interval[0] <= ans[-1][1]:
                ans[-1][1] = max(interval[1], ans[-1][1])
            else:
                ans.append(interval)
        return ans
"""
Спизжено
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        # 1. Find all non overlapping intervals
        currIdx = 0
        while currIdx < len(intervals) and intervals[currIdx][1] < newInterval[0]:
            res.append(intervals[currIdx])
            currIdx += 1

        # 2. Merge Overlapping intervals
        while currIdx < len(intervals) and intervals[currIdx][0] <= newInterval[1]:
            newInterval = [min(intervals[currIdx][0], newInterval[0]), max(intervals[currIdx][1], newInterval[1])]
            currIdx += 1
        res.append(newInterval)

        while currIdx < len(intervals):
            res.append(intervals[currIdx])
            currIdx += 1

        return res