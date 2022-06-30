// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        
        
        prev = [0 for price in prices]
        cur = [0 for price in prices]
        
        for t in range(1,k+1):
            maxThusFar = float('-inf')
            for D in range(1,len(prices)):
                maxThusFar = max(maxThusFar, prev[D-1] - prices[D-1])
                cur[D] = max(maxThusFar + prices[D],
                                   prev[D], 
                                   cur[D-1])
            
            prev = cur
            cur = [0 for price in prices]
        
        return prev[-1] if prev else 0