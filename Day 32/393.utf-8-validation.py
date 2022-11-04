#
# @lc app=leetcode id=393 lang=python3
#
# [393] UTF-8 Validation
#

# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0
        while i < n:
            if data[i] >> 3 == 30:
                if i + 3 >= n:
                    return False
                for j in range(1, 4):
                    if data[i + j] >> 6 != 2:
                        return False
                i += 4
            elif data[i] >> 4 == 14:
                if i + 2 >= n:
                    return False
                for j in range(1, 3):
                    if data[i + j] >> 6 != 2:
                        return False
                i += 3
            elif data[i] >> 5 == 6:
                if i + 1 >= n:
                    return False
                if data[i + 1] >> 6 != 2:
                    return False
                i += 2
            elif data[i] >> 7 == 0:
                i += 1
            else:
                return False
        return True
# @lc code=end

