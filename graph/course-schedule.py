from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Compute indegrees
        # Add all nodes with indegree 0 into the queue
        # BFS
        path = []
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
            path.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        print(path)
        return len(path) == numCourses

