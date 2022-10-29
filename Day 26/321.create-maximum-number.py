#
# @lc app=leetcode id=321 lang=python3
#
# [321] Create Maximum Number
#

# @lc code=start
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_subsequence(nums, k):
            stack = []
            for i, c in enumerate(nums):
                while stack and stack[-1] < c and len(stack) + len(nums) - i > k:
                    stack.pop()
                if len(stack) < k:
                    stack.append(c)
            return stack
        def merge(nums1, nums2):
            return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]
        return max(merge(max_subsequence(nums1, i), max_subsequence(nums2, k - i)) for i in range(k + 1) if i <= len(nums1) and k - i <= len(nums2))
# @lc code=end

