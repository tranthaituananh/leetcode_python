#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.map:
            return self.map[(s1, s2)]
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.map[(s1, s2)] = True
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                self.map[(s1, s2)] = True
                return True
        self.map[(s1, s2)] = False
        return False
    
    def __init__(self):
        self.map = {}
# @lc code=end

