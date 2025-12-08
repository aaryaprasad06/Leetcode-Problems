# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        temp= head
        while head is not None:
            stack.append(head.val)
            head= head.next
        while temp is not None:
            if temp.val != stack.pop():
                return False
            temp= temp.next 
        return True
