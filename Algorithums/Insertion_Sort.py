
"""
# Problem: Bubble Sort
# Difficulty: Easy
# Pattern: Sorting Algorithm

Problem:
Sort an array using the Bubble Sort algorithm.

Example:
nums = [5,4,3,2,1]
Ascending  -> [1,2,3,4,5]
Descending -> [5,4,3,2,1]

Idea:
- Compare adjacent elements
- Swap if they are in the wrong order
- After each pass, the largest (or smallest)
  element reaches its correct position

Revision:
- Learned Bubble Sort
- Implemented both ascending and descending versions
- Practiced adjacent swapping technique

Time Complexity: O(n²)
Space Complexity: O(1)
"""


class Solution(object):

    #! Ascending Order
    def Insertion_Sort_Asc(self,nums):
        
        for i in range(len(nums)):
            key = nums[i]
            j = i - 1
            while j>=0 and nums[j]> key:
                nums[j+1] = nums[j]
                j = j-1
            nums[j+1] = key
        return nums
    

    #! Descending Order

    def Insertion_Sort_Dsc(self,nums):
        for i in range(len(nums)):
            key = nums[i]
            j = i-1
            while j>=0 and nums[j]<key:
                nums[j+1] = nums[j]
                j = j-1
            nums[j+1] = key
        return nums
    

nums1 = [5,4,3,2,1]
s1 = Solution()
print(s1.Insertion_Sort_Asc(nums1))

nums2 = [1,2,3,4,5]
s2 = Solution()
print(s2.Insertion_Sort_Dsc(nums2))

