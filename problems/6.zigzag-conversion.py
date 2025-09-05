#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1:
            return s
        
        flag = 1 # 正序
        cur = 0
        all = ['' for _ in range(numRows)]        
        for i in s:
            if cur == 0:
                flag = 1
            elif cur==numRows-1:
                flag = -1
                
            all[cur]+=i
            cur+=flag
            
        return ''.join(all)
        
# @lc code=end

