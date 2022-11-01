#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity == 0:
            return True
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if jug1Capacity == 0 or jug2Capacity == 0:
            return targetCapacity in [0, jug1Capacity, jug2Capacity]
        return targetCapacity % self.gcd(jug1Capacity, jug2Capacity) == 0

    def gcd(self, a, b):  
        if a == 0: 
            return b 
        return self.gcd(b % a, a)
# @lc code=end

