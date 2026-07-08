# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        curr=head
        n=0
        while curr.next!= None:
            n+=1
            curr= curr.next
        n+=1

        k= k%n
        curr.next= head
        steps= n-k
        new_tail= head
        for _ in range(steps-1):
            new_tail= new_tail.next
        
        new_head= new_tail.next
        new_tail.next= None

        return new_head