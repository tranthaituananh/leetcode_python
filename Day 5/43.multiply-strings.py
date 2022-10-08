#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = '0'
        for i, n1 in enumerate(reversed(num1)):
            carry = 0
            tmp = ['0'] * i
            for n2 in reversed(num2):
                product = int(n1) * int(n2) + carry
                carry, digit = divmod(product, 10)
                tmp.append(str(digit))
            if carry > 0:
                tmp.append(str(carry))
            res = self.addStrings(res, ''.join(tmp[::-1]))
        return res
    
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        res = []
        for i in range(max(len(num1), len(num2))):
            n1 = int(num1[-i - 1]) if i < len(num1) else 0
            n2 = int(num2[-i - 1]) if i < len(num2) else 0
            sum = n1 + n2 + carry
            carry, digit = divmod(sum, 10)
            res.append(str(digit))
        if carry > 0:
            res.append(str(carry))
        return ''.join(res[::-1])
# @lc code=end

