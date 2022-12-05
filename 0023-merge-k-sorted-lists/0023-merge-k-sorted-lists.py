# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return
        
        while len(lists) > 1:
            merged_list = []
            
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i + 1) < len(lists) else None
                merged_list.append(self.merge(list1, list2))   
            lists = merged_list
        return lists[0]
     
        
    def merge(self, l1, l2):
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        temp_node = ListNode()
        temp = temp_node
        
        while l1 and l2:
            if l1.val <= l2.val:
                temp_node.next = l1
                l1 = l1.next
            else:
                temp_node.next = l2
                l2 = l2.next
            temp_node = temp_node.next
            
        if l1:
            temp_node.next = l1
            
        if l2:
            temp_node.next = l2
            
        return temp.next
        