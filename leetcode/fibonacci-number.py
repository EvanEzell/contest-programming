// https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        prev2 = 0
        prev1 = 1
        
        for i in range(2,n+1):
            cur = prev2 + prev1
            prev2 = prev1
            prev1 = cur
            
        return cur