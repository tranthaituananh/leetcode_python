#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return x == self.reverse(x)    
    def reverse(self, x: int) -> int:
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        return res    
# @lc code=end

