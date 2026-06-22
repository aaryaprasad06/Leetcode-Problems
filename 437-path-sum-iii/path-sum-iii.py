# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def countFrom(root, remaining):
            if not root:
                return 0
            count= 1 if remaining==root.val else 0
            count+= countFrom(root.left, remaining-root.val)
            count+= countFrom(root.right, remaining- root.val)
            return count
        
        if not root:
            return 0
        return countFrom(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)