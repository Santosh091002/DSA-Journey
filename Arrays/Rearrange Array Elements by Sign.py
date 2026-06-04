
"""
# Problem: Rearrange Array Elements by Sign
# Leetcode: 2149
# Difficulty: Medium
# Pattern: Array

Problem:
Rearrange the array so that positive and negative
numbers alternate, starting with a positive number.

Example:
nums = [3,1,-2,-5,2,-4]
Output = [3,-2,1,-5,2,-4]


Idea:
- Create a result array of the same size
- Place positive numbers at even indices
- Place negative numbers at odd indices
- Move indices by 2 after each placement

Revision:
- Used separate pointers for positive and
  negative positions
- Avoided extra shifting or swapping operations

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        pos_idx ,neg_idx = 0, 1
        for i in nums:
            if i > 0:
                res[pos_idx] = i
                pos_idx += 2
            else:
                res[neg_idx] = i
                neg_idx += 2
        return res

nums = [5,10,-3,-1,-10,6]
s = Solution()
print(s.rearrangeArray(nums))