class MyCircularQueue:

    class Node:
        def __init__(self, val: int):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        node = MyCircularQueue.Node(value)
        if self.size == 0:
            self.head = node
            self.tail = node
            node.next = node
            node.prev = node
        else:
            self.tail.next = node
            node.prev = self.tail
            node.next = self.head
            self.head.prev = node
            self.tail = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        else:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.tail.next = self.head.next
                self.head = self.head.next
                self.head.prev = self.tail
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.head.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.tail.val     

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.capacity == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()