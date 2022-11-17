#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])
        res = []
        if s_counter == p_counter:
            res.append(0)
        for i in range(len(p), len(s)):
            s_counter[s[i]] += 1
            s_counter[s[i - len(p)]] -= 1
            if s_counter[s[i - len(p)]] == 0:
                del s_counter[s[i - len(p)]]
            if s_counter == p_counter:
                res.append(i - len(p) + 1)
        return res
# @lc code=end
