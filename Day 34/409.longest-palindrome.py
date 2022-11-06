#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        for v in collections.Counter(s).values():
            res += v // 2 * 2
            if res % 2 == 0 and v % 2 == 1:
                res += 1
        return res
# @lc code=end

