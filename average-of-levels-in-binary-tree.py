// https://leetcode.com/problems/average-of-levels-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from statistics import mean

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        if root is None:
            return []
        
        curQueue = deque([root])
        nxtQueue = deque()
        num_nodes = 1
        total = 0
        
        result = []
        while curQueue:
            node = curQueue.popleft()
            total += node.val
            
            if node.left: nxtQueue.append(node.left)
            if node.right: nxtQueue.append(node.right)
                
            if not curQueue:
                result.append(total/num_nodes)
                curQueue = nxtQueue.copy()
                nxtQueue.clear()
                num_nodes = len(curQueue)
                total = 0
                
        return result            
                
            