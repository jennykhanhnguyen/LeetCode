class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.next = None
            self.prev = None
            self.val = val

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0
        self.dct = {}

    def move(self, node) -> None:
        if node == self.tail:
            return

        if node == self.head:
            self.head = node.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

    def get(self, key: int) -> int:
        if key not in self.dct:
            return -1

        node = self.dct[key]
        self.move(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dct:
            node = self.dct[key]
            node.val = value
            self.move(node)
            return

        node = self.Node(key, value)
        self.dct[key] = node

        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
            return

        if self.size == self.capacity:
            old = self.head
            del self.dct[old.key]
            self.head = old.next
            if self.head:
                self.head.prev = None
        else:
            self.size += 1

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)