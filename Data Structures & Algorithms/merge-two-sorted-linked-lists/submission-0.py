# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = ListNode(val=None, next=None)
        root = head
        while list1 or list2:
            new_head = ListNode(val=None , next = None)
            if not list1:
                new_head.val = list2.val
                list2 = list2.next    
            elif not list2:
                new_head.val = list1.val
                list1 = list1.next  
            else:
                is_list1_min = list1.val<list2.val
                if is_list1_min:
                    new_head.val = list1.val
                    list1 = list1.next
                else:
                    new_head.val = list2.val
                    list2 = list2.next
           
            head.next = new_head
            head = new_head
        return root.next 
        