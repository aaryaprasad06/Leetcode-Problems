# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1 and not list2:
            return
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            ans= ListNode(list1.val)
            ans.next= None
            list1= list1.next
        else:
            ans= ListNode(list2.val)
            ans.next= None 
            list2= list2.next
        head= ans
        while list1 and list2:
            if list1.val <= list2.val:
                node= ListNode(list1.val)
                node.next= None
                list1= list1.next
            else:
                node= ListNode(list2.val)
                node.next= None 
                list2= list2.next
            ans.next= node
            ans= ans.next
        while list1:
            node= ListNode(list1.val)
            node.next= None
            ans.next= node
            list1= list1.next
            ans= ans.next
        while list2:
            node= ListNode(list2.val)
            node.next= None
            ans.next= node
            list2= list2.next
            ans= ans.next
        return head