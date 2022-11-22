#
# @lc app=leetcode id=457 lang=python3
#
# [457] Circular Array Loop
#

# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue
            slow = fast = i
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[(fast + nums[fast]) % n] > 0:
                slow = (slow + nums[slow]) % n
                fast = (fast + nums[fast]) % n
                fast = (fast + nums[fast]) % n
                if slow == fast:
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True
        return False
# @lc code=end

