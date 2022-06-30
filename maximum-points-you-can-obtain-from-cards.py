// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        rightTot = 0
        for i in range(k):
            rightTot += cardPoints[len(cardPoints)-1-i]
        
        leftTot = 0
        maxPoints = 0
        for i in range(k):
            maxPoints = max(maxPoints, leftTot + rightTot)
            leftTot += cardPoints[i]
            rightTot -= cardPoints[len(cardPoints)-k+i]
        
        return max(maxPoints, leftTot)