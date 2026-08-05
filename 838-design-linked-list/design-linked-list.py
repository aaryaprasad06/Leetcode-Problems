class Node:
    def __init__(self, val):
        self.val= val
        self.next= None


class MyLinkedList:

    def __init__(self):
        self.head= None
        self.size= 0
        

    def get(self, index: int) -> int:
        if index<0 or index >= self.size:
            return -1
        ptr= self.head
        for i in range(index):
            ptr= ptr.next       

        return ptr.val
    
    def getkth(self, k: int) -> Node:
        if k<0 or k>= self.size:
            return None 
        ptr= self.head
        for _ in range(k):
            ptr= ptr.next 
        return ptr

    def addAtHead(self, val: int) -> None:
        newNode= Node(val)
        newNode.next= self.head 
        self.head= newNode
        self.size+=1

    def addAtTail(self, val: int) -> None:
        if self.size==0:
            self.addAtHead(val)
        else:
            ptr= self.getkth(self.size-1)
            newNode= Node(val)
            ptr.next= newNode
            self.size+=1


    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return
        if index==0:
            self.addAtHead(val)
            return
        if index== self.size:
            self.addAtTail(val)
            return
        ptr= self.getkth(index-1)
        newNode= Node(val)
        newNode.next= ptr.next
        ptr.next= newNode
        self.size+=1         

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return 
        if index==0:
            self.head= self.head.next
            self.size-=1
            return 
        ptr= self.getkth(index-1)
        ptr.next= ptr.next.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)