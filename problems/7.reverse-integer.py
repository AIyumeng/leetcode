# @before-stub-for-debug-begin
from python3problem7 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        
        flag = 1
        if x<0:
            flag = -1
            x = -x
            
        cur = 0
        while(x):
            temp = x % 10
            cur = cur * 10 + temp
            x = x//10
        
        cur = flag * cur
        if cur < -2**31 or cur > 2**31 - 1:
            return 0        
        return cur
            
# @lc code=end

