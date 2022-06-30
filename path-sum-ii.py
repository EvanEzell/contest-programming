// https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, tot, path, paths):
            if node:
                if not node.left and not node.right and tot == node.val:
                    paths.append(path + [node.val])
                dfs(node.left, tot - node.val, path + [node.val], paths)
                dfs(node.right, tot - node.val, path + [node.val], paths)
        
        paths = []
        dfs(root, targetSum, [], paths)
        return paths
            