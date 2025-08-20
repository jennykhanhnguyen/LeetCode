import queue

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = queue.Queue()
        arr = [[] for i in range(numCourses)]
        
        degree = [0]*(numCourses)
        for l,r in prerequisites:
            degree[l] += 1
            arr[r].append(l)

        for i,val in enumerate(degree):
            if val == 0:
                q.put(i)

        topo = []
        while q.qsize() > 0:
            u = q.get()
            for r in arr[u]:
                    degree[r] -= 1
                    if degree[r] == 0:
                        q.put(r)
            topo.append(u)
        
        if len(topo) != numCourses:
            return []
        return topo
            


