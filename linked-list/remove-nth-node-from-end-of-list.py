# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  
        cur = head 
        length = 0
        while cur:
            cur = cur.next
            length += 1
        if length == 1:
            head = None
            return head
        length = length - n - 1
        cur = head 
        print(length)
        while length > 0:
            cur = cur.next
            length -= 1
        print(cur.val)
        if length == -1:
            head = head.next
        elif cur.next and cur.next.next:
            cur.next = cur.next.next
        elif cur.next and cur.next.next == None:
            cur.next = None
        return head