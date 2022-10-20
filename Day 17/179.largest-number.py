#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            return int(b + a) - int(a + b)
        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(compare))
        return str(int(''.join(nums)))
# @lc code=end

