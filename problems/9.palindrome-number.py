#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        x = str(x)
        # return x == x[::-1]
        length = len(x)
        if length > 1:
            return x[:length//2] == x[-(length//2):][::-1]
        return True

# @lc code=end

