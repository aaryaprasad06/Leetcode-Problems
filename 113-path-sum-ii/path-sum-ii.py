# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        remaining= targetSum- root.val
        if not root.left and not root.right and remaining==0:
            return [[root.val]]
        if not root.left and not root.right:
            return []
        left= self.pathSum(root.left, remaining)
        right= self.pathSum(root.right, remaining)
        return [[root.val]+ path for path in left+right]

