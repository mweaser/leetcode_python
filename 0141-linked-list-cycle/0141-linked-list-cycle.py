# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next or not head.next.next:
            return False
        
        fast = head.next
        slow = head
        
        while fast.next and fast.next.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        
        return False
        
        
        
        