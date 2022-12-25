#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        win = []
        out = []
        for i in range(k):
            pos = bisect.bisect(win, nums[i])
            win.insert(pos, nums[i])
        if k % 2 != 0:
            out.append(win[k//2])
        else:
            out.append(float(win[k//2]+win[(k//2)-1])/2)
        for i in range(k, len(nums)):
            val = nums[i-k]
            win.remove(val)
            pos = bisect.bisect(win, nums[i])
            win.insert(pos, nums[i])
            if k % 2 != 0:
                out.append(win[k//2])
            else:
                out.append(float(win[k//2]+win[(k//2)-1])/2)
        return out
# @lc code=end
