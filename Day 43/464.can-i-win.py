#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        has_used = lambda flag, x: flag & (1<<x)
        is_odd = lambda x: x % 2 == 1
        @cache
        def can_player_win_on(target, bitflag):
            if target <= 0:
                return False
            for call_number in range(1, maxChoosableInteger+1):
                if has_used( bitflag, call_number ):
                    continue
                if not can_player_win_on(target - call_number, bitflag | (1<<call_number) ):
                    return True
            return False
        S = maxChoosableInteger * (maxChoosableInteger+1) // 2
        if S < desiredTotal:
            return False
        elif desiredTotal <= 0:
            return True
        elif S == desiredTotal and is_odd(maxChoosableInteger):
            return True
        return can_player_win_on(desiredTotal, bitflag=0 )        
# @lc code=end

