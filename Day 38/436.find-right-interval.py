#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = sorted([[intervals[i][0], i] for i in range(len(intervals))])
        end = sorted([[intervals[i][1], i] for i in range(len(intervals))])
        i = 0
        res = []
        for endVal, endIdx in end:
            while i < len(start) and (endVal > start[i][0]):
                i += 1
            if i < len(start):
                res.append(start[i][1])
            else:
                while len(res) < len(start):
                    res.append(-1)
        ans = []
        for i in range(len(end)):
            ans.append((end[i][1], res[i]))
        ans.sort()
        return [ele[1] for ele in sorted([[a[1], b] for a, b in zip(end, res)])]
# @lc code=end
