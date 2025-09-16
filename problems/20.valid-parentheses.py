#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

# import re
# class Solution:
#     def isValid(self, s: str) -> bool:
        
#         while s:
#             new_s = re.sub(r"\(\)", "", s)
#             new_s = re.sub(r"\[\]", "", new_s)
#             new_s = re.sub(r"\{\}", "", new_s)
#             if new_s == s:
#                 return False
#             s = new_s
#         return True

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack


# @lc code=end

