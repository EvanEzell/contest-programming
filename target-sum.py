// https://leetcode.com/problems/target-sum

class Solution:
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        cur = [0 for sum in range(-1000,1001)]
        next = [0 for sum in range(-1000,1001)]
        
        cur[nums[0]+1000] += 1
        cur[-nums[0]+1000] += 1
        
        for i in range(len(nums)-1):
            for sum in range(-1000,1000):
                if cur[sum+1000] > 0:
                    next[sum+nums[i+1]+1000] += cur[sum+1000]
                    next[sum-nums[i+1]+1000] += cur[sum+1000]

            cur = next
            next = [0 for sum in range(-1000,1001)]
        
        return cur[target+1000]
                
            
        
              
             

                    