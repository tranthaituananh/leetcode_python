#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#

# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        part1 = self.myPow(a, last)
        part2 = self.myPow(self.superPow(a, b), 10)
        return (part1 * part2) % 1337

    def myPow(self, x: int, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return x % 1337
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return (half * half) % 1337
        else:
            return (half * half * x) % 1337
# @lc code=end

