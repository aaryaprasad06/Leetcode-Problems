"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        que= deque([root])
        while que:
            ls= len(que)
            for i in range(ls):
                node= que.popleft()
                if i<ls-1:
                    node.next= que[0]
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root
        