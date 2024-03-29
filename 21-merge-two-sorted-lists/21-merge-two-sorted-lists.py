# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tempNode = ListNode(0)
        temp = tempNode
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
            
        if l1:
            temp.next = l1
            l1 = l1.next
        
        if l2:
            temp.next = l2
            l2 = l2.next
        
        return tempNode.next
        