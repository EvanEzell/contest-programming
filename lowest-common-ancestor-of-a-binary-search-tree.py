// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # if you find just one node, return the node
        # if you find both nodes from dfs on left and right, parent is lca
        
        def dfs(node):
            
            if node is None:
                return None
            if node == p:
                return p
            if node == q:
                return q
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            return node if left and right else left or right
        
        return dfs(root)