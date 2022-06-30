// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        while cur:
            if cur.left is None:
                # There is no left subtree, do not create any links
                # just print or decrement k
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right is not cur:
                    # Find predecessor of cur
                    pre = pre.right
                if pre.right is None:
                    # Create a temporary link from predecessor to cur, 1 pass
                    pre.right = cur
                    cur = cur.left
                else:
                    # Remove the link from predecessor to cur from 1 pass
                    # and print or decrement k
                    pre.right = None
                    k -= 1
                    if k == 0:
                        return cur.val
                    cur = cur.right