#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        
        num = 0
        sign = 1
        i = 0
        n = len(s)
        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        # Check for sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        # Convert digits to integer
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow
            if num > (2**31 - 1) // 10 or (num == (2**31 - 1) // 10 and digit > 7):
                return 2**31 - 1 if sign == 1 else -2**31
            num = num * 10 + digit
            i += 1
        return sign * num
# @lc code=end

