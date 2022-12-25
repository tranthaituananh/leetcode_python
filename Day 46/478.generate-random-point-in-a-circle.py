#
# @lc app=leetcode id=478 lang=python3
#
# [478] Generate Random Point in a Circle
#

# @lc code=start
class Solution:
        def __init__(self, radius: float, x_center: float, y_center: float):
            self.radius = radius
            self.x_center = x_center
            self.y_center = y_center
    
        def randPoint(self) -> List[float]:
            x = random.uniform(self.x_center - self.radius, self.x_center + self.radius)
            y = random.uniform(self.y_center - self.radius, self.y_center + self.radius)
            while (x - self.x_center) ** 2 + (y - self.y_center) ** 2 > self.radius ** 2:
                x = random.uniform(self.x_center - self.radius, self.x_center + self.radius)
                y = random.uniform(self.y_center - self.radius, self.y_center + self.radius)
            return [x, y]

# @lc code=end

