# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    
    # TLE
    # O(n^3) time
    # 310/315 cases passed (N/A)
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
        
    #     returns = set()
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             for k in range(j+1, len(nums)):
    #                 if nums[i]+nums[j]+nums[k]==0:
    #                     returns.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    #     return list(map(list, returns))

    
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     returns = set()
        
    #     for i in range(len(nums)-2):
    #         for j in range(i+1,len(nums)-1):
    #             left = j+1
    #             right = len(nums)-1
    #             while left <= right:
    #                 temp = (left + right)//2
    #                 if nums[i] + nums[j] + nums[temp] < 0:
    #                     left = temp + 1
    #                 elif nums[i] + nums[j] + nums[temp] > 0:
    #                     right = temp - 1
    #                 else:
    #                     returns.add((nums[i], nums[j], nums[temp]))
    #                     break
    #     return list(map(list, returns))
    
    
        # def threeSum(self, nums: List[int]) -> List[List[int]]:
        #     nums.sort()
        #     returns = set()
            
        #     for i in range(len(nums)-2):
        #         for j in range(i+1,len(nums)-1):
        #             left = j+1
        #             right = len(nums)
        #             while left < right:
        #                 temp = (left + right)//2
        #                 if nums[i] + nums[j] + nums[temp] < 0:
        #                     left = temp + 1
        #                 elif nums[i] + nums[j] + nums[temp] > 0:
        #                     right = temp
        #                 else:
        #                     returns.add((nums[i], nums[j], nums[temp]))
        #                     break
        #     return list(map(list, returns))

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        returns = set()
        
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    returns.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                    
        return list(map(list, returns))

# @lc code=end

