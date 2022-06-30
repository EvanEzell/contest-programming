// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addend = l1
        augend = l2
        
        result = ListNode()
        head = result
        carry = False
        
        while addend or augend:
            result.next = ListNode()
            result = result.next
            
            total = addend.val if addend else 0
            total += augend.val if augend else 0
            total += carry
            
            result.val = total if total < 10 else total - 10
            carry = total >= 10
            
            addend = addend.next if addend else None
            augend = augend.next if augend else None
            
        if carry:
            result.next = ListNode(val = 1)
            
        return head.next