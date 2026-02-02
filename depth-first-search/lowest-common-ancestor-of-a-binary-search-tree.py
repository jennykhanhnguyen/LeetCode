# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root.left or not root.right:
            print(root)
            return root
        if root.val >= p.val and root.val <= q.val:
            print(root)
            return root
        elif root.val <= p.val and root.val <= q.val:
            print(root)
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val >= p.val and root.val >= q.val:
            print(root)
            return self.lowestCommonAncestor(root.left, p, q)
            
