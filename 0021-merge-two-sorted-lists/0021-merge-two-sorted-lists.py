# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node = ListNode(0)
        curr = node
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        while l1 and l2:
            
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        while l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
        
        while l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next
        
        return node.next
            
            
        