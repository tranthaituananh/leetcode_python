#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_product = min_product = result = nums[0]
        for num in nums[1:]:
            max_product, min_product = max(num, max_product * num, min_product * num), min(num, max_product * num, min_product * num)
            result = max(result, max_product)
        return result
# @lc code=end

