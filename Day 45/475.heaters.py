#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        i = 0
        radius = 0
        for house in houses:
            while i < len(heaters) - 1 and abs(heaters[i] - house) >= abs(heaters[i + 1] - house):
                i += 1
            radius = max(radius, abs(heaters[i] - house))
        return radius
# @lc code=end

