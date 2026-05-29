"""
# Problem: Minimum Recolors to Get K Consecutive Black Blocks
# Leetcode: 2379
# Difficulty: Easy
# Pattern: Sliding Window

Problem:
Given a string of 'B' and 'W' blocks, find the minimum
number of white blocks that need to be recolored to get
k consecutive black blocks.

Example:
blocks = "WBBWWBBWBW", k = 7
Output = 3


Idea:
- Use a sliding window of size k
- Count white blocks ('W') inside the window
- The window with the minimum white count gives
  the answer

Improvement:
- Instead of checking every substring separately,
  maintain the count of white blocks while sliding
  the window

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        i = 0
        j = 0

        min_cnt = float("inf")
        cnt = 0

        while j < len(blocks):

            if blocks[j] == "W":
                cnt += 1

            # Maintain window size k
            if (j - i + 1) > k:
                if blocks[i] == "W":
                    cnt -= 1
                i += 1

            # Update answer when window size becomes k
            if (j - i + 1) == k:
                min_cnt = min(min_cnt, cnt)

            j += 1

        return min_cnt