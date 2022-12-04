// https://leetcode.com/problems/reorder-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head_ptr = ListNode(next = head)
        slow = head
        fast = head
        
        while True:
            if fast:
                fast = fast.next
                if fast:
                    fast = fast.next
                    slow = slow.next
                else:
                    break
            else:
                break
        
        prev = slow
        cur = prev.next
        prev.next = None
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        tail = prev
        
        while head != tail and head.next != tail:
            next_tail = tail.next
            tail.next = head.next
            head.next = tail
            head = tail.next
            tail = next_tail
        
        return head_ptr.next
        