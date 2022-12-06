#
# @lc app=leetcode id=467 lang=python3
#
# [467] Unique Substrings in Wraparound String
#

# @lc code=start
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0
        dp = [0] * 26
        dp[ord(p[0]) - ord('a')] = 1
        max_len = 1
        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i - 1]) == 1 or ord(p[i]) - ord(p[i - 1]) == -25:
                max_len += 1
            else:
                max_len = 1
            dp[ord(p[i]) - ord('a')] = max(dp[ord(p[i]) - ord('a')], max_len)
        return sum(dp)
# @lc code=end

