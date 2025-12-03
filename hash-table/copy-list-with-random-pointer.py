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
        if not head:
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
        for current in dic :
            if not current.random : 
                continue
            dic[current].random = dic[current.random]

        return dummy