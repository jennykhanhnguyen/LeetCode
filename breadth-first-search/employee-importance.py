"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import deque, defaultdict
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        rep = {}
        for obj in employees:
            rep[obj.id] = ((obj,obj.importance, obj.subordinates))
        queue = deque()
        obj = rep[id][0]
        queue.append(obj) # queue store object address
        total = 0
        while queue:
            size = len(queue)
            for i in range(size):
                addr = queue.popleft()
                total += addr.importance
                for neiID in addr.subordinates:
                    neiAddr = rep[neiID][0]
                    queue.append(neiAddr)           
        return total