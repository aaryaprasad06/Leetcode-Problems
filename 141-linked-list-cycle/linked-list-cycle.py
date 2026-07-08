# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while not head or not head.next:
            return False

        visited=[]

        curr= head
        while curr:
            if curr in visited:
                return True
            visited.append(curr)
            curr= curr.next 
        
        return False
