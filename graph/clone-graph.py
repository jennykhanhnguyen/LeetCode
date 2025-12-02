"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return node
        if node.val == 1 and node.neighbors == []:
            return Node(1)
        queue = deque()
        visited = [0]*101
        visited[node.val] = 1
        queue.append(node)
        newg = Node(1)
        dic = {}
        dic[1] = newg
        # print(node.val, node.neighbors)
        # for n in node.neighbors:
        #     print(n.val)
        while queue:
            size = len(queue)
            for i in range(size):
                pop = queue.popleft()   
                # print(pop.val)      
                for nei in pop.neighbors:    
                    if nei.val not in dic:
                        copy = Node(nei.val)
                        dic[nei.val] = copy
                    else :
                        copy = dic[nei.val]
                    # print(pop.val, copy.val)
                    dic[pop.val].neighbors.append(copy)
                    # newg.neighbors.append(copy)
                    # newg = newg.neighbors[0]
                    if visited[nei.val] == 0 and nei != None:
                        queue.append(nei)
                        visited[nei.val] = 1
                        
            # for pair in dic:
                # print(pair, dic[pair])

        return newg
