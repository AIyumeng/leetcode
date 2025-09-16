#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:

    def maxArea(self, height: list[int]) -> int:
        # 双指针
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

    # def maxArea(self, height: List[int]) -> int:
    #     # 暴力解法 TLE
    #     n = len(height)
    #     max_area = 0
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             area = min(height[i], height[j]) * (j - i)
    #             max_area = max(max_area, area)
    #     return max_area


# @lc code=end
