// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def preorder(node):
            
            
            if node.left is None and node.right is None:
                return node
            
            right = node.right
            left = node.left
            
            node.left = None
            if left:
                node.right = left
                tail = preorder(left)
                tail.right = right
            
            return preorder(right) if right else tail
            
        
        if root is None:
            return root
        
        preorder(root)
        return root