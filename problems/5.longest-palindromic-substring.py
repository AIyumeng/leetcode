#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start


class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     if not s:
    #         return ""
    #     n = len(s)
    #     dp = [[False] * n for _ in range(n)]
    #     start, max_length = 0, 1
    #     for i in range(n):
    #         dp[i][i] = True
    #     for i in range(n - 1):
    #         if s[i] == s[i + 1]:
    #             dp[i][i + 1] = True
    #             start = i
    #             max_length = 2
    #     for length in range(3, n + 1):
    #         if max_length < length - 2:
    #             break
    #         for i in range(n - length + 1):
    #             j = i + length - 1
    #             if s[i] == s[j] and dp[i + 1][j - 1]:
    #                 dp[i][j] = True
    #                 start = i
    #                 max_length = length
    #     return s[start:start + max_length]

    
    
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # 返回所有相等的连续子串
        substrings = []     # 存储所有相等连续子串的start和end
        start = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                continue
            substrings.append((start, i))
            start = i
        substrings.append((start, len(s)))
        
        max_string = ""
        
        for start, end in substrings:
            while start > 0 and end < len(s) and s[start-1] == s[end]:
                start -= 1
                end += 1
            max_string = max_string if len(max_string) > end - start else s[start:end]

        return max_string

# @lc code=end

