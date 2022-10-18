#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        res = 0
        for i in range(len(points)):
            dic = {}
            same = 0
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                    continue
                elif points[i][0] == points[j][0]:
                    slope = 'inf'
                else:
                    slope = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                dic[slope] = dic.get(slope, 0) + 1
            res = max(res, same + 1)
            for key in dic:
                res = max(res, dic[key] + same + 1)
        return res
# @lc code=end

