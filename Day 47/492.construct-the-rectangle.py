#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area**0.5), 0, -1):
            if area % i == 0:
                return [area // i, i]
# @lc code=end

