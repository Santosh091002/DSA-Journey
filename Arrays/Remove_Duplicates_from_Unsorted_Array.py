
"""
# Problem: Remove Duplicates from Unsorted Array
# Difficulty: Easy
# Pattern: Array + HashSet

Problem:
Remove duplicate elements from an unsorted array.

Example:
nums = [5,1,5,2,3,2,4,1,4]
Output = [5,1,2,3,4]


Idea:
- Use a HashSet to track seen elements
- Add an element to the result only if it
  has not appeared before

Revision:
- Solved in two ways:
  1. Using set() only (order not preserved)
  2. Using set() + result list (order preserved)

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def Remove_duplicates(self, nums):

        #! If elements order is not the priority
        # seen = set()
        # for i in nums:
        #     seen.add(i)
        
        # return list(seen)

        #! If order is Priority

        seen = set()
        res = []
        for i in nums:
            if i not in seen:
                seen.add(i)
                res.append(i)
        
        return res

nums = [5, 1, 5, 2, 3, 2, 4, 1, 4]
s = Solution()
print(s.Remove_duplicates(nums))
        

        
        