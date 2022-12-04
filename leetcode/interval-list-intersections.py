// https://leetcode.com/problems/interval-list-intersections

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        def intersection(interval1, interval2):
            maxStart, minEnd = max(interval1[0],interval2[0]), min(interval1[1],interval2[1])
            return [maxStart,minEnd] if maxStart <= minEnd else None
        
        results = []
        i = j = 0
        while i != len(firstList) and j != len(secondList):
            result = intersection(firstList[i], secondList[j])
            if result:
                results.append(result)
            
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return results
        