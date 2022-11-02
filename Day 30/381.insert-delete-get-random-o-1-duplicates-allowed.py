#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

# @lc code=start
class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.d = defaultdict(set)

    def insert(self, val: int) -> bool:
        if val in self.d:
            self.d[val].add(len(self.nums))
            self.nums.append(val)
            return False
        else:
            self.d[val] = {len(self.nums)}
            self.nums.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            idx = self.d[val].pop()
            if not self.d[val]:
                self.d.pop(val)
            if idx == len(self.nums) - 1:
                self.nums.pop()
            else:
                self.nums[idx] = self.nums[-1]
                self.d[self.nums[idx]].remove(len(self.nums) - 1)
                self.d[self.nums[idx]].add(idx)
                self.nums.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
