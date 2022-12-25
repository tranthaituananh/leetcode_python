#
# @lc app=leetcode id=481 lang=python3
#
# [481] Magical String
#

# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        s = ["1", "2", "2"]
        for i in range(2, n):
            p = s[-1] == "2"
            if (s[-1] == '2'):
                s += ["1"] * int(s[i])
            else:
                s += ["2"] * int(s[i])
            if (len(s) > n):
                break
        return s[:n].count('1')
# @lc code=end
