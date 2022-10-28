#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
class BITTree:

    def __init__(self, nums: List[int]):
        self.bi_tree = [0] * (len(nums) + 1)
        self.n = len(nums)
        for i in range(self.n):
            self.update(i + 1, nums[i])

    def update(self, index: int, value: int):
        while index <= self.n:
            self.bi_tree[index] += value
            index += self.low_bit(index)

    def get_sum(self, index: int) -> int:
        prefix = 0
        while index > 0:
            prefix += self.bi_tree[index]
            index -= self.low_bit(index)
        return prefix

    @staticmethod
    def low_bit(bit: int) -> int:
        return bit & -bit


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bi_tree = BITTree(nums)

    def update(self, i: int, val: int):
        self.bi_tree.update(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.bi_tree.get_sum(right + 1) - self.bi_tree.get_sum(left)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

