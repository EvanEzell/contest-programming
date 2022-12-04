// https://leetcode.com/problems/path-sum-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(seen, node, pathSum):
            
            pathSum += node.val
            if pathSum - targetSum in seen and seen[pathSum - targetSum]:
                self.count += seen[pathSum - targetSum]
            seen[pathSum] += 1
            
            if node.left is None and node.right is None:
                seen[pathSum] -= 1
                if seen[pathSum] == 0: del seen[pathSum]
                return
            
            if node.left:
                dfs(seen, node.left, pathSum)
            if node.right:
                dfs(seen, node.right, pathSum)
        
            seen[pathSum] -= 1
    
        if root is None:
            return 0
        
        dfs(Counter([0]), root, 0)
        return self.count