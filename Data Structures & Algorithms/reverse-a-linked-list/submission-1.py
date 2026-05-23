# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## re wrote today myself
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        node = head
        prev = None

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        return prev