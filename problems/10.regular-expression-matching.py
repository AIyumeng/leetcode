# @before-stub-for-debug-begin
from python3problem10 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start

""" import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.fullmatch(p, s) is not None """


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]
        
    
    # def isMatch(self, s: str, p: str) -> bool:
    #     matched = [-1]
    #     last_pp = None
    #     for i, pp in enumerate(p):
    #         new_matched = []
    #         if pp == ".":
    #             last_pp = "."
    #             if i + 1 < len(p) and p[i + 1] == "*":
    #                 continue
    #             for match in matched:
    #                 new_matched.append(match + 1)
    #         elif pp == "*":
    #             if last_pp == ".":
    #                 new_matched = [i for i in range(min(matched), len(s))]
    #             else:
    #                 for match in matched:
    #                     new_matched.append(match)
    #                     while match + 1 < len(s) and s[match + 1] == last_pp:
    #                         new_matched.append(match + 1)
    #                         match += 1
    #         else:
    #             if i + 1 < len(p) and p[i + 1] == "*":
    #                 last_pp = pp
    #                 continue
    #             for match in matched:
    #                 if match + 1 < len(s) and s[match + 1] == pp:
    #                     new_matched.append(match + 1)
    #             last_pp = pp

    #         matched = new_matched
    #         if not matched:
    #             return False

    #     return len(s) - 1 in matched


# @lc code=end
