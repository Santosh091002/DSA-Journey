"""
# Problem: Two Sum
# Leetcode: 1
# Difficulty: Easy
# Pattern: HashMap

Problem:
Given an array nums and a target, return the indices
of two numbers whose sum equals the target.

Example:
nums = [2,7,11,15], target = 9
Output = [0,1]


Idea:
- Store each number and its index in a hashmap
- For every number, find its complement
  (target - current number)
- If complement exists in hashmap, return indices

Revision:
- Practiced HashMap lookup approach
- Avoided brute force nested loops

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in h:
                return [h[comp], i]

            h[nums[i]] = i