# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(head , i):

            if not head:
                return None
            print(i)
            head.next = rec(head.next , i)
            
            i[0] -=1
            if i[0]==0:
                return head.next
            return head
        
        return rec(head,[n])