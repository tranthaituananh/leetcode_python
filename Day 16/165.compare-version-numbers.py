#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        for i in range(max(len(v1), len(v2))):
            v1_num = int(v1[i]) if i < len(v1) else 0
            v2_num = int(v2[i]) if i < len(v2) else 0
            if v1_num > v2_num:
                return 1
            elif v1_num < v2_num:
                return -1
        return 0
# @lc code=end

