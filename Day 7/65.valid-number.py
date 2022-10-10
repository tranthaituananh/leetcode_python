#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if 'inf' in s.lower() or s.isalpha():
                return False
            if float(s) or float(s) >= 0:
                return True
        except:
            return False
# @lc code=end

