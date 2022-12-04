// https://leetcode.com/problems/binary-tree-maximum-path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = root.val
        
        def dfs(node):
            
            if not node:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            self.max = max(self.max,
                           leftMax + node.val + rightMax)
            
            return max(leftMax + node.val, rightMax + node.val)
        
        dfs(root)
        return self.max