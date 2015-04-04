# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        res, stack, current = [], [], root
        while stack or current:
            if current:
                stack.append(current)
                res.append(current.val)
                current = current.left
            else:
                parent = stack.pop()
                current = parent.right
        return res
