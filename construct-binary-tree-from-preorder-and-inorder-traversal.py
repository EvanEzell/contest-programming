// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        self.left = 0
        self.right = len(inorder)
        
        self.map = {val: index for index, val in enumerate(inorder)}
        
        def recurse(left, right):
            if right - left <= 0:
                return None
            if right - left == 1:
                self.index += 1
                return TreeNode(inorder[left])
            
            root = TreeNode(preorder[self.index])
            self.index += 1
            
            root_index = self.map[root.val]
            root.left = recurse(left, root_index)
            root.right = recurse(root_index + 1, right)
            
            return root
        
        return recurse(0, len(inorder))