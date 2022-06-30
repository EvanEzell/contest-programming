// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        prevMax = -prices[0]
        
        for today in range(1,len(prices)):
            profit = max(prevMax + prices[today], profit)
            prevMax = max(prevMax, profit - prices[today])
         
        return profit