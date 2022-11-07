#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        result = []
        carry = 0
        for i in range(len(num1)):
            if i < len(num2):
                digit = int(num1[i]) + int(num2[i]) + carry
            else:
                digit = int(num1[i]) + carry
            carry = digit // 10
            digit = digit % 10
            result.append(str(digit))
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])
# @lc code=end

