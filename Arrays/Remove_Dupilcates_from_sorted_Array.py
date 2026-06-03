
"""
# Problem: Remove Duplicates from Sorted Array
# Leetcode: 26
# Difficulty: Easy
# Pattern: Two Pointers

Problem:
Remove duplicates from a sorted array in-place
and return the number of unique elements.

Example:
nums = [0,0,1,1,1,2,2,3,3,4]
Output = 5


Idea:
- Keep one pointer (j) at the last unique element
- Traverse with another pointer (i)
- When a new unique element is found,
  place it after j and move j forward

Revision:
- First thought of using a set to count unique elements
- Improved to the in-place Two Pointer approach
  required by LeetCode

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def Remove_Duplicates(self,nums):
        
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        #! Accepted if requirement is only unique elements count
        # seen = set()
        # for i in range(n):
        #     seen.add(nums[i])
        
        # return len(seen)

        #! Leetcode variant
        j = 0
        i = j+1

        while i < n:
            if nums[j] < nums[i]:
                j+=1
                nums[i],nums[j] = nums[j],nums[i]
            i += 1
        
        return j+1


nums = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
print(s.Remove_Duplicates(nums))
