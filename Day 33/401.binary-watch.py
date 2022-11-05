#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        return [f'{h}:{m:02}' for h in range(12) for m in range(60) if (bin(h) + bin(m)).count('1') == turnedOn]
# @lc code=end
