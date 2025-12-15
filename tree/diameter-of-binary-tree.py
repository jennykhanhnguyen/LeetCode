# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # bfs to get the leave node with deepest level and create graph
        graph = {}
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        level = {}
        queue = deque()
        queue.append(root)
        lv = -1
        numnode = 0
        while queue:
            size = len(queue)
            lv += 1
            for i in range(size):
                node = queue.popleft()
                # numnode += 1
                level[node] = lv
                if node.left:
                    queue.append(node.left)
                    if node.left not in graph:
                        graph[node.left] = []
                    if node not in graph:
                        graph[node] = []
                    graph[node].append(node.left)
                    graph[node.left].append(node)
                if node.right:
                    queue.append(node.right)
                    if node.right not in graph:
                        graph[node.right] = []
                    if node not in graph:
                        graph[node] = []
                    graph[node].append(node.right)
                    graph[node.right].append(node)
        # lv = level of the deepest leaf
        for address, val in level.items():
            if len(graph[address]) == 1 and level[address] == lv:
                end = address

        # bfs to calculate the longest diameter
        visited = set()
        res = -1
        queue.append(end)
        visited.add(end)
        while queue:
            size = len(queue)
            res += 1
            for i in range(size):
                address = queue.popleft()
                for nei in graph[address]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)


        return res




        # for address, val in level.items():
        #     if len(graph[address]) == 1:
        #         start = address
        #         break

        # def dfs(address, res):  
        #     nonlocal maxres        
        #     maxres = max(res, maxres)
        #     # print(maxres)
        #     if address == end:
        #         return
        #     for nei in graph[address]:
        #         if nei not in visited:
        #             visited.add(nei)
        #             dfs(nei, res+1)
        #             visited.remove(nei) 
        # dfs(start, 0)

