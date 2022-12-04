// https://leetcode.com/problems/minimum-area-rectangle

# Put points into two multi-sets keyed on their x coordinate and y coordinate
# [[1,1],[1,3],[3,1],[3,3],[2,2]]
# x_map: {1: 1,3
#         2: 2
#         3: 1,3
#        }

# y_map: {1: 1,3
#         2: 2
#         3: 1,3
#        }

# O(n) time

# always order line from smallest to largest y
# also a multiset
# vertical lines: {(1,3): 1, 3
#                 }
# 1 -> 3 at x = 1
# 1 -> 3 at x = 3
# if there are no veritcal lines that begin and end on same
# endpoints, we can't make a rectangle
# O(n^2) pairs

# iterate through possible vertical line pairs,
# if their is corresponding horizontal lines connecting them
# compute area of rectangle
# O(n^2) pairs, constant amount of work to check if there are corresponding horizontal lines

# if area of rectangle is smaller than minimum area seen thus far
# set the new minimum

# O(n^2) time
# O(n^2) space

# Put all points in set O(n) time, O(n) space
# For all possible diagonals (diagonal is just a pair of any two points), check
# if their are matching points to make a rectangle. O(n^2) diagonals, O(1) time to check for matching points
# Compute area if valid rectangle and set new minimum area if we found one O(1)
# O(n^2) time, O(n) space

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        minArea = float('inf')
        point_set = {(x,y) for x,y in points}
        for x1, y1 in points:
            for x2, y2 in points:
                # only check diagonal from bottom left to upper right
                # otherwise, we are checking every diagonal twice
                if x1 < x2 and y1 < y2:
                    if (x1,y2) in point_set and (x2,y1) in point_set:
                        minArea = min(minArea, (y2 - y1) * (x2 - x1))
        return minArea if minArea != float('inf') else 0
                        
                    
                    
                
        