// https://leetcode.com/problems/best-sightseeing-pair

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        prev = values[0]
        result = 0
        
        for i in range(1,len(values)):
            cur = max(prev, values[i] + i)
            result = max(result, prev + values[i] - i)
            prev = cur
        
        return result