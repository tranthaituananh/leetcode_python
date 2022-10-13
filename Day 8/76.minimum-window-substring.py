#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_dict = {}
        for c in t:
            t_dict[c] = t_dict.get(c, 0) + 1
        s_dict = {}
        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        for c in t_dict:
            if c not in s_dict or s_dict[c] < t_dict[c]:
                return ""
        left = 0
        right = 0
        min_left = 0
        min_right = len(s)
        while right < len(s):
            if s[right] in t_dict:
                t_dict[s[right]] -= 1
                while all([t_dict[c] <= 0 for c in t_dict]):
                    if right - left < min_right - min_left:
                        min_left = left
                        min_right = right
                    if s[left] in t_dict:
                        t_dict[s[left]] += 1
                    left += 1
            right += 1
        return s[min_left:min_right + 1]
# @lc code=end

