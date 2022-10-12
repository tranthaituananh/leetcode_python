#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            if not stack or h > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and h <= heights[stack[-1]]:
                    j = stack.pop()
                    k = stack[-1] if stack else -1
                    max_area = max(max_area, heights[j] * (i - k - 1))
                stack.append(i)
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            max_area = max(max_area, heights[j] * (len(heights) - k - 1))
        return max_area
# @lc code=end

