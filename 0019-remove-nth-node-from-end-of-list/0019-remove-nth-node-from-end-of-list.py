# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp_node = ListNode(0, head)
        l = temp_node
        r = head
        
        while n:
            r = r.next
            n -= 1
            
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        return temp_node.next 