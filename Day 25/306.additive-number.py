#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num)):
            for j in range(i + 1, len(num)):
                if self.isAdditive(num[:i], num[i:j], num[j:]):
                    return True
        return False

    def isAdditive(self, num1, num2, num):
        if (num1.startswith('0') and len(num1) > 1) or (num2.startswith('0') and len(num2) > 1):
            return False
        if not num:
            return True
        sum = str(int(num1) + int(num2))
        if not num.startswith(sum):
            return False
        return self.isAdditive(num2, sum, num[len(sum):])
# @lc code=end

