#
# @lc app=leetcode id=479 lang=python3
#
# [479] Largest Palindrome Product
#

# @lc code=start
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        lower = 10 ** (n - 1)
        for i in range(upper, lower - 1, -1):
            palindrome = int(str(i) + str(i)[::-1])
            for j in range(upper, lower - 1, -1):
                if palindrome // j > upper:
                    break
                if palindrome % j == 0:
                    return palindrome % 1337
        return -1
# @lc code=end

