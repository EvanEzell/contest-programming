// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        self.visited = set()

        def dfs(node):
            if node is None:
                return False
            if node in self.visited:
                return True
            self.visited.add(node)
            return dfs(node.next)
        
        return dfs(head)