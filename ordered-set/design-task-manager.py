import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_to_user = dict()
        self.task_to_priority = dict()
        self.heap = [] # store pair of priority and taskId
                       # max heap
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_to_user[taskId] = userId
        self.task_to_priority[taskId] = priority
        heapq.heappush(self.heap, (-priority, -taskId))
        
    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_to_priority[taskId] = newPriority
        heapq.heappush(self.heap, (-newPriority, -taskId))
        
    def rmv(self, taskId: int) -> None:
        self.task_to_user.pop(taskId, None)
        self.task_to_priority.pop(taskId, None)

    def execTop(self) -> int:
        while self.heap:
            priority, taskId = heapq.heappop(self.heap)
            
            priority = -priority
            taskId = -taskId
            
            if taskId in self.task_to_priority and self.task_to_priority[taskId] == priority:
                del self.task_to_priority[taskId]
                user = self.task_to_user[taskId]
                del self.task_to_user[taskId]
                return user

        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()