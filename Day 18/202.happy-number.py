#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n in seen:
                return False
            seen.add(n)
        return True
# @lc code=end

