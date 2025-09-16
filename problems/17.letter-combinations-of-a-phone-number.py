# @before-stub-for-debug-begin
from python3problem17 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start


from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        d2s = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        output = []

        for digit in digits:
            if digit in d2s:
                output.append(d2s[digit])

        return ["".join(combo) for combo in product(*output)]


# @lc code=end
