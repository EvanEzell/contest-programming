// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def overlaps(interval1, interval2):
            return interval2[1] >= interval1[0] and interval2[0] <= interval1[1]
        
        def merge(interval1, interval2):
            return [min(interval1 + interval2),
                    max(interval1 + interval2)]
            
        intervals.sort()
        result = []
        
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if overlaps(cur, intervals[i]):
                cur = merge(cur, intervals[i])
            else:
                result.append(cur)
                cur = intervals[i]
        result.append(cur)
                
        return result