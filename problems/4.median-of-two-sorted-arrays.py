# @before-stub-for-debug-begin
from python3problem4 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start


class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

    #     # 让nums1更长, 对nums2二分查找
    #     if len(nums1) < len(nums2):
    #         nums1, nums2 = nums2, nums1
    #     l1, l2 = len(nums1), len(nums2)

    #     mid = (l1 + l2) // 2
    #     left = 0
    #     right = l2
    #     while left <= right:
    #         temp = (left + right) // 2
    #         n1 = nums1[mid - temp - 1] if mid - temp > 0 else -inf
    #         n2 = nums2[temp - 1] if temp > 0 else -inf
    #         n1_nxt = nums1[mid - temp] if mid - temp < l1 else inf
    #         n2_nxt = nums2[temp] if temp < l2 else inf
    #         if n1_nxt >= n2 and n2_nxt >= n1:
    #             break
    #         elif n2_nxt < n1:
    #             # temp 小了
    #             left = temp + 1  # 不使用 temp+1 向下取整可能会死循环
    #         else:
    #             right = temp
    #     flag = (l1 + l2) % 2
    #     if flag:
    #         n1 = nums1[mid - temp]
    #         n2 = nums2[temp] if temp < l2 else inf
    #         return n1 if n1 < n2 else n2
    #     else:
    #         n1_prev = nums1[mid - temp - 1] if mid - temp >= 1 else -inf
    #         n2_prev = nums2[temp - 1] if temp >= 1 else -inf
    #         n1 = nums1[mid - temp] if mid - temp < l1 else inf
    #         n2 = nums2[temp] if temp < l2 else inf
    #         return (max(n1_prev, n2_prev) + min(n1, n2)) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # 让nums1更长, 对nums2二分查找
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        l1, l2 = len(nums1), len(nums2)

        mid = (l1 + l2) // 2
        left = 0
        right = l2
        # while True:
        while left <= right:
            temp = (left + right) // 2
            n1 = nums1[mid - temp - 1] if mid - temp > 0 else -inf
            n2 = nums2[temp - 1] if temp > 0 else -inf
            n1_nxt = nums1[mid - temp] if mid - temp < l1 else inf
            n2_nxt = nums2[temp] if temp < l2 else inf
            if n1_nxt >= n2 and n2_nxt >= n1:
                break
            elif n2_nxt < n1:
                left = temp + 1  
            else:
                right = temp - 1
        flag = (l1 + l2) % 2
        if flag:
            n1 = nums1[mid - temp]
            n2 = nums2[temp] if temp < l2 else inf
            return n1 if n1 < n2 else n2
        else:
            n1_prev = nums1[mid - temp - 1] if mid - temp >= 1 else -inf
            n2_prev = nums2[temp - 1] if temp >= 1 else -inf
            n1 = nums1[mid - temp] if mid - temp < l1 else inf
            n2 = nums2[temp] if temp < l2 else inf
            return (max(n1_prev, n2_prev) + min(n1, n2)) / 2

# @lc code=end
