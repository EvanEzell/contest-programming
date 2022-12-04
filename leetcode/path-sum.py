// https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(node, tot):
            
            tot += node.val
            
            if not node.left and not node.right: # leaf node
                return tot == targetSum
            
            leftResult = helper(node.left, tot) if node.left else False
            rightResult = helper(node.right, tot) if node.right else False
            
            return leftResult or rightResult
        
        return helper(root, 0) if root else False