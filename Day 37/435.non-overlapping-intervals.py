#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = float('-inf')
        count = 0
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            else:
                count += 1
        return count
# @lc code=end

