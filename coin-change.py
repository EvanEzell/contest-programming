// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        minCoins = [float('inf')] * (amount + 1)
        minCoins[0] = 0
        
        for tot in range(1,amount+1):
            for coin in coins:
                if tot - coin >= 0:
                    minCoins[tot] = min(minCoins[tot], 1 + minCoins[tot-coin])
        
        return minCoins[amount] if minCoins[amount] != float('inf') else -1
                    