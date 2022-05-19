# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LinkedList:
    def __init__(self):
        self.head=None
    def addTail(self,ele):
        if self.head is None:
            node=ListNode(ele)
            self.head=node
            return self.head
        itr=self.head
        while itr.next:
            itr=itr.next
        node=ListNode(ele)
        itr.next=node
        return self.head
class Solution:
    def reverselist(self,head):
        prev=None
        current=head
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        head=prev
        return head
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1=self.reverselist(l1)
        l2=self.reverselist(l2)
        string1=""
        string2=""
        itr,ptr=l1,l2
        while itr:
            string1+=str(itr.val)
            itr=itr.next
        while ptr:
            string2+=str(ptr.val)
            ptr=ptr.next
        res=list(str(int(string1)+int(string2)))[::-1]
        obj=LinkedList()
        for i in range(len(res)):
            head=obj.addTail(res[i])
        return head