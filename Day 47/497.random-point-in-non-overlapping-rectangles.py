#
# @lc app=leetcode id=497 lang=python3
#
# [497] Random Point in Non-overlapping Rectangles
#

# @lc code=start
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        self.total = 0
        for rect in rects:
            self.total += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.weights.append(self.total)

    def pick(self) -> List[int]:
        target = random.randint(0, self.total - 1)
        left, right = 0, len(self.rects) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.weights[mid] <= target:
                left = mid + 1
            else:
                right = mid
        rect = self.rects[left]
        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3])
        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# @lc code=end

