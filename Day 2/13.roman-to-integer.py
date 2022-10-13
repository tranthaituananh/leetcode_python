#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = 0
        for i in range(len(val)):
            while s.startswith(rom[i]):
                s = s[len(rom[i]):]
                res += val[i]
        return res
# @lc code=end

