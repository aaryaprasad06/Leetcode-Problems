# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        
        que= deque([root])
        bottom_left=0
        while que:
            ls= len(que)
            for i in range(ls):
                node= que.popleft()
                if i==0:
                    bottom_left= node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
        return bottom_left

                