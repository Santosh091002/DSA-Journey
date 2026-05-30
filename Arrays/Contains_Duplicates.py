"""
# Problem: Contains Duplicate
# Leetcode: 217
# Difficulty: Easy
# Pattern: Array + HashSet

Problem:
Return True if any value appears at least twice
in the array, otherwise return False.

Example:
nums = [1,2,3,1]
Output = True


Idea:
- Use a set to track seen numbers
- If a number is already in the set,
  duplicate found

Revision:
- Practiced HashSet lookup
- Avoided brute force comparisons

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        