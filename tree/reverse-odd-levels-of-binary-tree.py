# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import math
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        lv = 0
        dic = {}
        while queue:
            dic.clear()
            lv += 1
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    if lv % 2 != 0:
                        dic[2*i] = (node.left,node.left.val)
                if node.right:
                    queue.append(node.right)
                    if lv % 2 != 0:
                        dic[2*i+1] = (node.right,node.right.val)
            half = math.ceil(len(dic)/2)
            for j in range(half):
                dic[j][0].val, dic[len(dic)-j-1][0].val = dic[len(dic)-j-1][0].val, dic[j][0].val
        return root
                    

