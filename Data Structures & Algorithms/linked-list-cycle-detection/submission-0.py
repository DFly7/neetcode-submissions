# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        node = head

        visited = set()

        while node and node.next:
            if node.val in visited:
                return True
            
            visited.add(node.val)
            node = node.next
        
        return False