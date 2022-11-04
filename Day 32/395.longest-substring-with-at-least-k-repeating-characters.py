#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        counter = collections.Counter(s)
        for c in counter:
            if counter[c] < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return n
# @lc code=end

