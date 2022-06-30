// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_ptr = ListNode(next = head)
        
        while n:
            head = head.next
            n -= 1
        
        trail = head_ptr
        while head:
            head = head.next
            trail = trail.next
        
        trail.next = trail.next.next
        
        return head_ptr.next