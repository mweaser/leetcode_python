# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        l, r = head, head
        
        while r and r.next:
            l = l.next
            r = r.next.next
               
        curr = l
        prev = None
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        first, second = head, prev
        
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp
            
            tmp = second.next
            second.next = first
            second = tmp
        
        