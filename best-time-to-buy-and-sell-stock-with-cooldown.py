// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        bought = float('-inf')
        sold = float('-inf')
        cooled = 0
        
        for price in prices:
            buying = max(bought, cooled - price)
            selling = bought + price
            cooling = max(cooled, sold)
            
            bought, sold, cooled = buying, selling, cooling
        
        return max(sold, cooled)
        
