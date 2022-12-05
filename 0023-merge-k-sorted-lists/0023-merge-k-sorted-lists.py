# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
     
        ele = []
        
        for i in range(len(lists)):
            curr = lists[i]
            while curr:    
                ele.append(curr.val)
                curr = curr.next
                
        ele.sort()
        print("ele:", ele)
        
        temp_node = ListNode(0)
        temp = temp_node
        
        for i in range(len(ele)):
            curr = ListNode(ele[i])
            temp_node.next = curr
            temp_node = temp_node.next
            
        return temp.next
        
        
            