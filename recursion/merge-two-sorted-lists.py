# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        
        res = ListNode()
        curr1 = list1
        curr2 = list2
        if curr1.val < curr2.val:
            res = curr1
            curr1 = curr1.next
        else:
            res = curr2
            curr2 = curr2.next
        temp = res
        while curr1 and curr2:
            if curr1.val < curr2.val:
                temp.next = curr1
                curr1 = curr1.next
                temp = temp.next
            else:
                temp.next = curr2
                curr2 = curr2.next
                temp = temp.next
        while curr1:
            temp.next = curr1
            curr1 = curr1.next
            temp = temp.next
        while curr2:
            temp.next = curr2
            curr2 = curr2.next
            temp = temp.next

        return res
