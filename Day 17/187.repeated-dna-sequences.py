#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, repeated = set(), set()
        for i in range(len(s) - 9):
            ten = s[i:i + 10]
            if ten in seen:
                repeated.add(ten)
            seen.add(ten)
        return list(repeated)
# @lc code=end

