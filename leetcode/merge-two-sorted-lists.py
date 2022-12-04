// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(next = list1)
        prev1 = head
        cur1 = list1
        cur2 = list2
        
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                prev1 = cur1
                cur1 = cur1.next
            else: # merge in cur2
                nxt2 = cur2.next
                prev1.next = cur2
                cur2.next = cur1
                cur2 = nxt2
                prev1 = prev1.next
        
        if cur2:
            while cur2:
                nxt2 = cur2.next
                prev1.next = cur2
                cur2.next = cur1
                cur2 = nxt2
                prev1 = prev1.next
            
        return head.next