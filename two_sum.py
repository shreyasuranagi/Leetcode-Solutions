# Problem: Two Sum (LeetCode #1)
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
#
# Description:
# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target. You may assume 
# that each input would have exactly one solution.

# Complexity:
# Time: O(n) - Single pass through the hash map
# Space: O(n) - Storing elements in the dictionary

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        out=[]
        for i in range(len(nums)):
            if (target-nums[i]) in (nums[:i]+nums[i+1:]):
            
                out.append(i)
                out.append(nums.index(target-nums[i],i+1))
                return out

# SOLUTION EXPLAINED:
'''
we need to find the other element after subtracting fromt he target element
'''