"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        dic = {}
        dummy = Node(head.val) # dummy = copy
        temp = dummy           # temp = copy traversal
                               # head = original 
        cur = head             # cur = original traversal
        while cur:
            temp.val = cur.val
            dic[cur] = temp
            if cur.next:
                copy = Node(cur.next.val)
                temp.next = copy
            else:
                temp.next = None
            temp = temp.next
            cur = cur.next
        temp = dummy
        cur = head
        while cur:
            if cur.random:
                temp.random = dic[cur.random]
            else:
                temp.random = None
            temp = temp.next
            cur = cur.next

        return dummy