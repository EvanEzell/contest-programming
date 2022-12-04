// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        curLevel = deque([root])
        nextLevel = deque()
        
        zigzag = [[root.val]]
        vals = []
        
        leftToRight = False
        while curLevel:
            node = curLevel.pop()

            if leftToRight:
                if node.left: 
                    nextLevel.append(node.left)
                    vals.append(node.left.val)
                if node.right: 
                    nextLevel.append(node.right)
                    vals.append(node.right.val)
            else:
                if node.right: 
                    nextLevel.append(node.right)
                    vals.append(node.right.val)                
                if node.left: 
                    nextLevel.append(node.left)
                    vals.append(node.left.val)
                    
            if not curLevel and vals:
                zigzag.append(vals)
                curLevel = nextLevel.copy()
                nextLevel = deque()
                vals = []
                leftToRight = not leftToRight
              
        return zigzag