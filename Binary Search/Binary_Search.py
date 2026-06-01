
"""
# Problem: Binary Search
# Difficulty: Easy
# Pattern: Binary Search

Problem:
Given a sorted array and a target value,
return the index of the target.
If the target is not present, return -1.

Example:
nums = [1,2,3,4,5,6,7,8,9]
target = 5
Output = 4


Idea:
- Find the middle element
- If target is found, return its index
- If target is smaller, search left half
- If target is larger, search right half
- Repeat until found or search space becomes empty

Revision:
- Practiced Binary Search on a sorted array
- Reduced search space by half in each step

Time Complexity: O(log n)
Space Complexity: O(1)
"""


nums = [1,2,3,4,5,6,7,8,9]
target = 5

class Solution:
    def Binary_Search(self,nums,target):
        low = 0
        high = len(nums) -1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    

s = Solution()
r = s.Binary_Search(nums,target)
print(r)

