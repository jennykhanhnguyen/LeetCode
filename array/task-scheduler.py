import heapq
from collections import Counter, deque

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dct = Counter(tasks)
        heap = [-val for val in dct.values()]   
        heapq.heapify(heap)

        cooldown = deque()   
        time = 0

        while heap or cooldown:
            time += 1

            if heap:
                count = heapq.heappop(heap)
                count += 1 

                if count != 0:
                    cooldown.append((count, time + n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])

        return time