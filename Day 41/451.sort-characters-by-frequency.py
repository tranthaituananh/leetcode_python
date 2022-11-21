#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        counter = Counter(s)
        return ''.join([char * times for char, times in counter.most_common()])
# @lc code=end

