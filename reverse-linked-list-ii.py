// https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        prev = headptr = ListNode(next=head)
        cur = head
        
        # find leftTail
        for _ in range(1,left):
            prev = cur
            cur = cur.next
        leftTail = prev
        leftNode = cur
        
        # reverse middle segment
        for _ in range(left,right):
            next = cur.next
            
            cur.next = prev
            prev = cur
            cur = next
        
        rightNode = cur
        rightHead = cur.next
        
        cur.next = prev
            
        leftTail.next = rightNode
        leftNode.next = rightHead
        
        return headptr.next