// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkTree(pnode, qnode):
            
            if not pnode and not qnode:
                return True
            if not pnode or not qnode:
                return False
            if pnode.val != qnode.val:
                return False
            
            return (checkTree(pnode.left, qnode.left) and
                    checkTree(pnode.right, qnode.right))
        
        def dfs(node):
            
            if node is None:
                return False
            
            return (checkTree(node, subRoot) or
                    dfs(node.left) or
                    dfs(node.right))
        
        return dfs(root)