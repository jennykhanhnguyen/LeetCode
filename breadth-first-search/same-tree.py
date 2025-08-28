# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]              # start with a pair of root nodes
        while stack:                  # process until stack is empty
            p, q = stack.pop()        # take one pair of nodes
            if p or q:                # if at least one of them is not None
                if not p or not q or p.val != q.val:
                    return False      # structure mismatch OR values differ
                stack.append((p.left, q.left))   # check left children
                stack.append((p.right, q.right)) # check right children
        return True                   # no mismatches found
