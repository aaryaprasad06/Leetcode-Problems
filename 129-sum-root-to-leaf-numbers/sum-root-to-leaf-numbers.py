# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not(root.left) and not(root.right):
            return root.val
        num= root.val
        def solve(root, current):
            if not root:
                return 0
            current= current* 10+ root.val
            if not root.left and not root.right:
                return current
            if root.left and not root.right:
                return solve(root.left, current)
            elif root.right and not root.left:
                return solve(root.right, current)
            else:
                return solve(root.left, current)+ solve(root.right, current)


        return solve(root.left, num) + solve(root.right, num)
        
        