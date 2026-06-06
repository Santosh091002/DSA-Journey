
"""
# Problem: Selection Sort
# Difficulty: Easy
# Pattern: Sorting

Problem:
Sort an array in ascending or descending order
using the Selection Sort algorithm.

Example:
nums = [4,2,1,5,3]
Ascending  -> [1,2,3,4,5]
Descending -> [5,4,3,2,1]


Idea:
- Find the minimum (or maximum) element
  in the unsorted portion
- Swap it with the current position
- Repeat for all positions

Revision:
- Implemented both Ascending and Descending versions
- Practiced finding min/max element and swapping

Time Complexity: O(n²)
Space Complexity: O(1)
"""


nums = [1,2,4,2,1,4,3,1,8,9,4,3,5,3]


class Solution(object):

    #! Ascending Order

    def Selection_Sort_Asc(self,nums):
        for i in range(0,len(nums)):
            min_idx = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i],nums[min_idx] = nums[min_idx],nums[i]
        return nums
    


    #! Descending Order

    def Selection_Sort_Dsc(self,nums):
        for i in range(0 , len(nums)):
            max_idx = i
            for j in range(i+1,len(nums)):
                if nums[j] > nums[max_idx]:
                    max_idx = j
            nums[i],nums[max_idx] = nums[max_idx],nums[i]
        return nums


s1 = Solution()
print(s1.Selection_Sort_Asc(nums))

print(s1.Selection_Sort_Dsc(nums))
