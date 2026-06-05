
"""
# Problem: Longest Consecutive Sequence
# Leetcode: 128
# Difficulty: Medium
# Pattern: Array + HashSet

Problem:
Find the length of the longest consecutive
sequence in an unsorted array.

Example:
nums = [100,4,200,1,3,2]
Output = 4

Explanation:
Sequence = [1,2,3,4]


Idea:
- Store all numbers in a set
- Start counting only if the number is the
  beginning of a sequence (num - 1 not in set)
- Keep extending the sequence using num + 1
- Track the maximum length

Revision:
- First thought was sorting the array
- Improved to HashSet approach with O(n) time
- Avoided checking the same sequence multiple times

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        my_set = set()
        mx_cnt = 0
        for num in nums:
            my_set.add(num)
        
        for num in my_set:
            if num - 1 not in my_set:
                cnt = 1
                c_num = num
                while c_num + 1 in my_set:
                    cnt += 1
                    c_num += 1
                if cnt > mx_cnt:
                    mx_cnt = cnt
        return mx_cnt

nums = [0,3,7,2,5,8,4,6,0,1]
s = Solution()
print(s.longestConsecutive(nums))


          


        