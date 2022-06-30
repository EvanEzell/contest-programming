// https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        queue = deque([(p,q)])
        
        while queue:
            pnode, qnode = queue.popleft()
            
            if not pnode and not qnode:
                continue
            if not pnode or not qnode:
                return False
            if pnode.val != qnode.val:
                return False
            
            queue.append((pnode.left, qnode.left))
            queue.append((pnode.right, qnode.right))
        
        return True