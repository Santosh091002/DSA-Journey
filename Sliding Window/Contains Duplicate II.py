"""
# Problem: Contains Duplicate II
# Leetcode: 219
# Difficulty: Easy
# Pattern: Sliding Window + HashMap

Problem:
Return True if same number appears within distance k.

Example:
nums = [1,2,3,1], k = 3
Output = True


Idea:
- Store elements inside hashmap
- Maintain window size <= k
- If current element already exists in hashmap,
  duplicate found


Improvement:
- Earlier checked slices repeatedly
- Optimized using sliding window hashmap


Time Complexity: O(n)
Space Complexity: O(k)
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        i = 0
        j = 0
        h = {}

        while j < len(nums):

            # Maintain window size
            if abs(i - j) > k:
                h.pop(nums[i])
                i += 1

            # Duplicate found
            if nums[j] in h:
                return True
            else:
                h[nums[j]] = 1

            j += 1

        return False