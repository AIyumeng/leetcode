#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        char_set = set()
        left = 0
        max_length = 0
        
        right = 0
        while right < len(s):
            if s[right] in char_set:
                char_set.remove(s[left])
                left+=1        
            else:
                char_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
        # for right in range(len(s)):
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left += 1
        #     char_set.add(s[right])
        #     max_length = max(max_length, right - left + 1)

        return max_length
    
    
# @lc code=end

