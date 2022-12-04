class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
	if not len(prices):
	    return 0
	
	prevProfits = [0 for d in prices]
	curProfits = [0 for d in prices]

	for t in range(1,k+1):
	    maxThusFar = float('-inf')

	    for d in range(1,len(prices)):
		maxThusFar = max(maxThusFar, prevProfits[d-1] - prices[d-1])
		curProfits[d] = max(curProfits[d-1], maxThusFar + prices[d])
		
	    prevProfits,curProfits = curProfits,prevProfits
			
        return prevProfits[-1]
