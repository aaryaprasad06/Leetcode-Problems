# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        node= root
        while node:
            if val==node.val:
                break
            elif val< node.val:
                node= node.left
            else:
                node= node.right
            
        
        return node
        
        # que=deque([node])
        # res=[]
        # while que:
        #     ls= len(que)
        #     for i in range(ls):
        #         n=que.popleft()
        #         if n.left:
        #             que.append(n.left)
        #         if n.right:
        #             que.append(n.right)
        #         res.append(n.val)
        # return res
        