# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        carry = 0
        if not l1:
            return l2
        if not l2:
            return l1
        
        tempNode = ListNode(0)
        temp = tempNode
        
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2: 
                val2 = l2.val
            else:
                val2 = 0 
                
            carry, out = divmod(val1 + val2 + carry, 10)
            temp.next = ListNode(out)
            temp = temp.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return tempNode.next