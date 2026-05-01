# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        i = n
        def rec(head  ):
            nonlocal i
            if not head:
                return None
            
            head.next = rec(head.next )
            
            i -=1
            if i==0:
                return head.next
            return head
        
        return rec(head)