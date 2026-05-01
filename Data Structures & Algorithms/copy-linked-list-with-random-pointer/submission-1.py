"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        mapping = {}
        tail = head
        while tail:
            mapping[tail] = Node(x = tail.val)
            tail = tail.next
        new_head = mapping[head]
        tail = head
        while tail:
            tmp = mapping[tail]
            tmp.next = mapping.get(tail.next , None)
            
            tmp.random = mapping.get(tail.random , None)
            
            tail = tail.next

        return new_head