// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxDepth = 0
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def findMaxDepth(node=root, depth=self.maxDepth):
            
            if node is None:
                return
            
            self.maxDepth = max(self.maxDepth, depth)
            
            findMaxDepth(node.left, depth + 1)
            findMaxDepth(node.right, depth + 1)
        
        def findSubtree(node=root, depth=0):
            
            if node is None:
                return None
            
            if depth == self.maxDepth:
                return node
            
            left = findSubtree(node.left, depth + 1)
            right = findSubtree(node.right, depth + 1)
            
            if left is None and right is None:
                return None
            
            if left and right:
                return node
            
            return left if left else right
            
        findMaxDepth()
        return findSubtree()
        
            
            