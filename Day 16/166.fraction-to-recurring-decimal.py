#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        result = []
        if numerator * denominator < 0:
            result.append('-')
        numerator, denominator = abs(numerator), abs(denominator)
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(result)
        result.append('.')
        remainder_map = {}
        while remainder != 0:
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], '(')
                result.append(')')
                break
            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        return ''.join(result)
# @lc code=end

