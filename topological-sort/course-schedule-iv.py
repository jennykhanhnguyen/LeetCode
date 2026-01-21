from collections import defaultdict
class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # build graph
        # make a list of dictionary
        # topo sort on graph to update the global list
        # look up
        ans = []
        empty_dct = []
        for i in range(100):
            empty_dct.append(set())
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
                empty_dct[nei].add(node)
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        for left, right in queries:
            if left in empty_dct[right]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

