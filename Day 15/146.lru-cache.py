#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.used = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.used.remove(key)
            self.used.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        n = len(self.used)
        if key in self.cache:
            self.used.remove(key)
            self.used.append(key)
            self.cache[key] = value
        elif n < self.capacity:
            self.used.append(key)
            self.cache[key] = value
        else:
            self.cache.pop(self.used[0])
            self.used.pop(0)
            self.used.append(key)
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

