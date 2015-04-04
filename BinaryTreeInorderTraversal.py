# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        res, stack, current = [],[],root
        while stack or current:
            if current:
                stack.append(current)
                current=current.left
            else:
                parent=stack.pop()
                res.append(parent.val)
                current=parent.right
        return res
                
