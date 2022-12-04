// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        cur = deque([root])
        nxt = deque()
        
        result = []
        
        while cur and root:
            
            result.append([node.val for node in cur])
            
            while cur:
                node = cur.popleft()

                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)

            cur = nxt
            nxt = deque()
        
        return result