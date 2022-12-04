// https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[i:]
            
            if newInterval[0] > interval[1]:
                result.append(interval)
            else:
                newInterval = [min(newInterval + interval),
                               max(newInterval + interval)]
        
        result.append(newInterval)
        return result