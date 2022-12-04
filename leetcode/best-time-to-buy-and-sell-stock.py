// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxThusFar = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxThusFar = max(maxThusFar, price - minPrice)
        
        return maxThusFar