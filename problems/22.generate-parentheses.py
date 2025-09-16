# @before-stub-for-debug-begin
from python3problem22 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    
    def check(self, s):
        left, right = 0, 0
        for ss in s:
            if ss=='(':
                left+=1
            elif ss==')':
                right+=1
        return left,right
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        s = ['']
        final = []
        while s:
            new_s = []
            for ss in s:
                left, right = self.check(ss + '(')
                if left ==right and left==n:
                    final.append(ss+'(')
                elif left<=n:
                    new_s.append(ss+'(')
                if ss and left-1>right:
                    left, right = self.check(ss + ')')
                    if left ==right and left==n:
                        final.append(ss+')')
                    else:
                        new_s.append(ss+')')
            s = new_s
            
        return final
        
        
        
        
        
        
        
        
# @lc code=end

