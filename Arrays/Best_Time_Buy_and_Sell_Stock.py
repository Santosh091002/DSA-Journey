"""
# Problem: Best Time to Buy and Sell Stock
# Leetcode: 121
# Difficulty: Easy
# Pattern: Array / Greedy

Problem:
Find the maximum profit that can be made by
buying and selling a stock once.

Example:
prices = [7,1,5,3,6,4]
Output = 5


Idea:
- Track the minimum price seen so far
- Calculate profit for each day
- Update maximum profit whenever a better profit is found

Revision:
- Instead of checking all buy-sell pairs,
  kept track of the minimum price while traversing once

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        max_Profit = 0
        min_Price = float("inf")
        for i in range(n):
            if prices[i] < min_Price:
                min_Price = prices[i]
            
            Profit = prices[i] - min_Price
            if Profit > max_Profit:
                max_Profit = Profit
        
        return max_Profit

nums = [7,2,1,5,4,6,8]
s = Solution()
res = s.maxProfit(nums)
print(res)
