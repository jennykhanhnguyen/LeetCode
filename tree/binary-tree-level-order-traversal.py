# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# queue = [root]
# lvl = 0
# while queue is not empty : 
#     size = queue.size()
#     lvl += 1
#     for 0 -> size : 
#         pop_out current = queue.pop()
#         queue.push(current->left)
#         ...
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = deque()
        res = []
        lv = 0
        queue.append(root)
        while queue:
            lv += 1
            size = len(queue)
            temp = []
            for i in range(size):
                node = queue.popleft()
                temp.append(node.val)
                # print(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # print(node)
            res.append(temp)
        return res