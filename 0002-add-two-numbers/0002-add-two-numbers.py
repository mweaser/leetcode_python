# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         first = ""
#         second = ""
        
#         while l1:
#             first += str(l1.val)
#             l1 = l1.next
        
#         while l2:
#             second += str(l2.val)
#             l2 = l2.next
            
        first = ""
        second = ""
        
        while l1:
            first = str(l1.val) + first
            l1 = l1.next
        
        while l2:
            second = str(l2.val) + second
            l2 = l2.next
        
        total = str(int(first) + int(second))
        l = list(total)
        l.reverse()
        
        temp_node = ListNode(0)
        temp = temp_node
        
        while l:
            val = l.pop(0)
            new = ListNode(int(val))
            temp_node.next = new
            temp_node = temp_node.next
        
        return temp.next
        
        
        
        