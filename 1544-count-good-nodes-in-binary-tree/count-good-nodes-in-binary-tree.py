# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_so_far= root.val
        def findNodes(root, max_so_far):
            if not root:
                return 0
            if root.val >= max_so_far:
                count=1
                max_so_far= root.val
            else:
                count=0
            count+= findNodes(root.left, max_so_far)
            count+= findNodes(root.right, max_so_far)
            return count
        
        left= findNodes(root.left, max_so_far)
        right= findNodes(root.right, max_so_far)
        
        return 1+ left+ right