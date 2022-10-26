#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        return self.helper(num)

    def helper(self, num):
        if num < 20:
            return self.lessThan20(num)
        if num < 100:
            return self.tens(num)
        if num < 1000:
            return self.hundreds(num)
        if num < 1000000:
            return self.thousands(num)
        if num < 1000000000:
            return self.millions(num)
        return self.billions(num)

    def lessThan20(self, num):
        return "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()[num - 1]

    def tens(self, num):
        return "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()[num // 10 - 2] + " " + self.helper(num % 10) if num % 10 else "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()[num // 10 - 2]

    def hundreds(self, num):
        return self.helper(num // 100) + " Hundred " + self.helper(num % 100) if num % 100 else self.helper(num // 100) + " Hundred"

    def thousands(self, num):
        return self.helper(num // 1000) + " Thousand " + self.helper(num % 1000) if num % 1000 else self.helper(num // 1000) + " Thousand"

    def millions(self, num):
        return self.helper(num // 1000000) + " Million " + self.helper(num % 1000000) if num % 1000000 else self.helper(num // 1000000) + " Million"

    def billions(self, num):
        return self.helper(num // 1000000000) + " Billion " + self.helper(num % 1000000000) if num % 1000000000 else self.helper(num // 1000000000) + " Billion"
# @lc code=end

