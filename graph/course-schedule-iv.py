from collections import defaultdict
class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        hm = []
        for i in range(100):
            hm.append([0]*100)
        ans = []
        indegree = [0]*numCourses
        queue = deque()
        graph = defaultdict(list)
        for left, right in prerequisites:
            indegree[right] += 1
            graph[left].append(right)
        for ind, node in enumerate(indegree):
            if node == 0:
                queue.append(ind)
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                for i in range(numCourses):
                    if hm[i][node] == 1:
                        hm[i][nei] = 1
                hm[node][nei] = 1
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        for left, right in queries:
            if hm[left][right] == 1:
                ans.append(True)
            else:
                ans.append(False)
        return ans

