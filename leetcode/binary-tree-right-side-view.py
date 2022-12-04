// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# this feels like a level order traversal problem
# keep a queue of the current level nodes
# and a queue of the next level nodes

# For example
# view = [1,3,4]
# cur_queue = []
# nxt_queue = []

# O(n) time complexity
# O(n) space complexity, perfect binary tree could have n/2 nodes at last level

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        view = []
        cur_queue = deque([root])
        nxt_queue = deque()
        
        while cur_queue:
            node = cur_queue.popleft()
            
            if node.left:
                nxt_queue.append(node.left)
            if node.right:
                nxt_queue.append(node.right)
            
            if not cur_queue:
                view.append(node.val)
                cur_queue = nxt_queue
                nxt_queue = deque()

        
        return view