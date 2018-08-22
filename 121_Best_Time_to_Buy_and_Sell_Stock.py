# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# 1) elegant single-pass O(N) solution
import sys
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # init two variables to store lowest value and max_profit
        min_val = sys.maxsize
        max_profit = 0

        # one pass iteartion, O(N) complexity
        for price in prices:
            if price < min_val:
                min_val = price
            elif price - min_val > max_profit:
                max_profit = price - min_val

        return max_profit

# 2) brute force
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        length = len(prices)

        for i in range(length-1):
            for j in range(i+1,length):
                if prices[j]-prices[i] > result: result = prices[j]-prices[i]
        return(result)

