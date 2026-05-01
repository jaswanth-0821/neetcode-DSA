# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_current_value_and_update(self,l1,l2):
        v1 = 0
        if l1 : 
            v1 = l1.val
            l1 = l1.next
        v2 = 0
        if l2 :
            v2 = l2.val
            l2 = l2.next
        return v1,v2,l1,l2
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        final_answer = ListNode(0)
        return_answer = final_answer
        remaining = 0
     
        while l1 or l2:
            
            v1,v2 , l1,l2 = self.get_current_value_and_update(l1,l2)
           
            sum_ = v1 + v2 +remaining

            answer = sum_ % 10
            remaining = sum_ //10
           
            final_answer.val = answer
            if l1 or l2 or remaining:
                final_answer.next  = ListNode(0)
                final_answer = final_answer.next
        
        if remaining:
            final_answer.val = remaining
        
        return return_answer

        

