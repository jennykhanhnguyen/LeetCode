class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        cut = slow.next
        slow.next = None

        temp = cut
        prev = None
        while temp:
            tmpnxt = temp.next
            temp.next = prev
            prev = temp
            temp = tmpnxt
        
        # # prev = [5,4]
        # # head = [1,2,3]

        first = head
        second = prev

        while first and second:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2

        return None

