#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1
        }
        cur = 0
        for i in range(len(s)-1):
            if dict[s[i]]>=dict[s[i+1]]:
                cur+=dict[s[i]]
            else:
                cur-=dict[s[i]]
        return cur+dict[s[-1]]
                
        
# @lc code=end

