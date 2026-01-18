# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
      
        def calculate_height(node):

            # Base case: empty node has height 0
            if node is None:
                return 0
          
            # Recursively calculate heights of left and right subtrees
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
          
            # Check if any subtree is unbalanced or if current node violates balance condition
            if (left_height == -1 or 
                right_height == -1 or 
                abs(left_height - right_height) > 1):
                return -1  # Return -1 to indicate unbalanced tree
          
            # Return height of current subtree (1 + maximum height of children)
            return 1 + max(left_height, right_height)
      
        # Tree is balanced if height calculation doesn't return -1
        return calculate_height(root) >= 0