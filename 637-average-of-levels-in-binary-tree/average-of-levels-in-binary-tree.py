# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        que= deque([root])
        res=[]

        while que:
            level_size= len(que)
            s=0
            for i in range(level_size):
                node= que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                s= s+node.val
            res.append(s/level_size)
        return res
        
