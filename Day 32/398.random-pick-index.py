#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for idx, num in enumerate(nums):
            self.d[num].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self.d[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end
