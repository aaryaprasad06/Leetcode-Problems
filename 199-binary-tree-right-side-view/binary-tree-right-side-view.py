# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res=[]
        que= deque([root])

        while que:
            level_size= len(que)
            left=0
            for i in range(level_size):
                node= que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(node.val)
        return res


        