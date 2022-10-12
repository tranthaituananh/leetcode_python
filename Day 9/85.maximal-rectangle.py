#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area

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

