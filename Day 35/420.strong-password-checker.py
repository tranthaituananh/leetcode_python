#
# @lc app=leetcode id=420 lang=python3
#
# [420] Strong Password Checker
#

# @lc code=start
from itertools import zip_longest


class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        length = len(password)
        additions_needed = 3 - contains_conditions_satisfied(password)
        if length < 6:
            return max(6-length, additions_needed)
        if length <= 20:
            breaks_needed = 0
            current_streak = 1
            for c1, c2 in zip_longest(password, password[1:]):
                if c1 == c2:
                    current_streak += 1
                else:
                    breaks_needed += current_streak//3
                    current_streak = 1
            return max(breaks_needed, additions_needed)
        breaks_needed = 0
        current_streak = 1
        streaks = [0, 0, 0]
        for c1, c2 in zip_longest(password, password[1:]):
            if c1 == c2:
                current_streak += 1
            else:
                if current_streak >= 3:
                    breaks_needed += current_streak//3
                    streaks[current_streak % 3] += 1
                current_streak = 1
        deletions_needed = length - 20
        deletions_remaining = deletions_needed
        if streaks[0]:
            breaks_not_needed = min(streaks[0], deletions_remaining)
            deletions_remaining -= breaks_not_needed
            breaks_needed -= breaks_not_needed
        if streaks[1]:
            breaks_not_needed = min(streaks[1], deletions_remaining//2)
            deletions_remaining -= 2*breaks_not_needed
            breaks_needed -= breaks_not_needed
        breaks_needed -= min(breaks_needed, deletions_remaining//3)
        return deletions_needed + max(breaks_needed, additions_needed)


def contains_conditions_satisfied(s: str) -> int:
    return (any(c.islower() for c in s) +
            any(c.isupper() for c in s) +
            any(c.isdigit() for c in s))
# @lc code=end
